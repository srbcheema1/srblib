#! /usr/bin/env python3
import hashlib
import os
import sys
import time

from .path import abs_path

def _hash_file(fname):
    fname = abs_path(fname)
    BLOCKSIZE = 65536
    hasher = hashlib.md5()
    with open(fname, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return hasher.hexdigest()


def _dfs_dir(path):
    content = os.listdir(path)
    dir_hash = "+"
    for a in content:
        a = os.path.join(path,a)
        if os.path.isdir(a):
            val = _dfs_dir(a)
            dir_hash += val
        elif os.path.isfile(a):
            dir_hash += '-'
            dir_hash += str(_hash_file(a))
    return dir_hash


def str_hash(inp):
    inp = str(inp)
    return str(hashlib.md5(inp.encode('utf-8')).hexdigest())

def path_hash(path):
    path = abs_path(path)
    if not os.path.exists(path):
        raise Exception('Path not found ' + path)
    if os.path.isfile(path):
        return _hash_file(path)
    dir_hash = _dfs_dir(path)
    return str_hash(dir_hash)

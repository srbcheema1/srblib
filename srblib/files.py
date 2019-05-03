import os
import shutil

from .path import abs_path
from .colour import Colour


def verified_file(file_path):
    '''
    returns abs_path if exists or raise exception
    '''
    file_path = abs_path(file_path)
    if not os.path.isfile(file_path):
        raise Exception('No such file : ' + file_path)
    return file_path

def verify_folder(folder,debug=False):
    '''
    similar to mkdir -p
    '''
    folder = abs_path(folder)
    if not os.path.exists(folder):
        if(debug): print('creating folder '+ folder)
        os.makedirs(folder,exist_ok=True)
    elif os.path.isfile(folder):
        if(debug): print('there exists file of same name')

def verify_file(file_path,debug=False):
    '''
    verifies a file. if it doesn't exists creates one
    '''
    file_path = abs_path(file_path)
    parent_dir = os.path.join(file_path,os.pardir)
    verify_folder(parent_dir)
    if not os.path.exists(file_path):
        if(debug): print('creating file '+ file_path)
        file_ = open(file_path, 'w')
        file_.close()
    elif os.path.isdir(file_path):
        if(debug): print('there exists folder of same name')

def remove(path,debug=False):
    '''
    removes a folder/file of given path.
    works recursively for folders
    '''
    path = abs_path(path)
    if not os.path.exists(path):
        return
    if os.path.isfile(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)
    else:
        Colour.print('unknown path : '+path,Colour.RED)



def file_name(file_path):
    file_path = abs_path(file_path)
    items = file_path.split('/')[-1]
    return items

def file_extension(file_path):
    file_name_ = file_name(file_path)
    if(file_name_[0] == '.'): file_name_ = file_name_[1:]
    if('.' in file_name_):
        return file_name_.split('.')[-1]
    else:
        return ''

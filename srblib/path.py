#!/usr/bin/env python3
import os
from sys import argv

from .system import get_os_name

def _reactified(path):
    '''
    assumes that path has forward slashes in it
    and no slash at the end
    '''
    drive = None
    nodes = path.split("/")
    if(nodes[0] != ''): drive = nodes[0] # for windows it will pick C: or D:

    direc = []
    nodes = nodes[1:] # remove everthing before first slash, its contained in drive
    for node in nodes:
        if(node=='.'): continue
        elif(node=='..'):
            if(len(direc)>0):
                direc.pop()
            else:
                raise Exception("Cant go beyond base directory, arg: "+path)
        else: direc.append(node)

    path = ""
    for item in direc:
        path = path + "/"
        path = path + item

    if(drive): path = drive + path # add drive again
    return path


def _abs_path_unix(path):
    pwd = str(os.getcwd())#always return without / at end;
    home_path = os.getenv("HOME")#always return without / at end

    if(len(path)>1 and path[-1]=='/'):#remove last backslash
        path=path[:-1]
    if(path[0]=='/'):
        return reactified(path)
    if(path[0]=='~'):
        return reactified(home_path + path[1:])
    if(path[0]!='.'):
        return reactified(pwd + '/' + path)

    return reactified(pwd +'/'+ path)



def _abs_path_windows(path):
    '''
    takes path in any slash but return only in forward slash
    '''
    pwd = str(os.getcwd())#always return without / at end except drives ex C:\
    home_path = os.getenv("userprofile")#always return without / at end, ex: C:\User\srb
    if(home_path==''):home_path = 'C:\\User\\testing'

    # make paths better looking
    pwd = _change_slash(pwd)
    pwd = _reactified(pwd)
    home_path = _change_slash(home_path)
    path = _change_slash(path)
    if(len(path)>1 and path[-1]=='/'):#remove last backslash
        path=path[:-1]

    if(path[0]=='/'):
        raise Exception('windows path cant start with slash')
    if(path[0]=='~'):
        ans = _reactified(home_path + path[1:])
    elif(len(path)>1 and path[1]==':'): #path is of type C:.... or D:.....
        ans = _reactified(path)
    else:
        ans = _reactified(pwd +'/'+ path)

    return ans

def _change_slash(path,shash='/'):
    ans = ""
    for a in path:
        if a in ['/','\\']:
            ans+=slash
        else:
            ans+=a
    return ans

'''
takes relative path as string argument as a path in linux
returns absolute path without '/' at end
means it will write /home/srb instead of /home/srb/

its more helpful when dealing with paths of files.
both the paths will be in sync as both wont have / at end
'''

def abs_path(path,slash='/'):
    os_name = get_os_name()
    if(os=='windows'):
        path = _abs_path_windows(path)
        return _change_slash(path,slash)
    else:
        return _abs_path_unix(path)


if __name__ == "__main__":
    '''
    point to be noted:
    if you run as ./abs_path.py hello\world
    you will get different values in argv[1]
    windows:
        hello\world
    unix:
        helloworld
    '''
    print(argv[1])
    print(abs_path(argv[1],'\\'))

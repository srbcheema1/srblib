import os
import subprocess

from .util import line_adder, dump_output
from .colour import Colour

def _get_supported_distros(dependency_map):
    supported_distros = set()
    for rules in dependency_map.values():
        for key in rules.keys():
            supported_distros.add(key)
    return supported_distros


def _recognise_distro(distros=['ubuntu']):
    try:
        p = subprocess.Popen(['uname','-a'], stdout=subprocess.PIPE)
        out = p.stdout.read().decode('utf-8').lower()
        for d in distros:
            if d in out:
                return d
        return None
    except:
        return None

def _get_installed_package_mangers(available_package_managers):
    installed_package_managers = set()
    for apm in available_package_managers:
        if is_installed(apm):
            installed_package_managers.add(apm)
    return installed_package_managers


def is_installed(soft):
    help_opt = ' --help '
    a = os.system(soft + help_opt + dump_output)
    if a == 0 or a == 256:
        '''
        0 means return 0
        256 means return 1, generally for those who dont have --help
        if command not found it will return 32512
        '''
        return True
    return False


def install_arg_complete(app_name):
    if is_installed('register-python-argcomplete'):
        line = 'eval "$(register-python-argcomplete '+app_name+')"'
        filename = os.environ['HOME'] + '/.bashrc'
        line_adder(filename,line)


def install_dependencies(dependency_map, verbose = False):
    supported_distros = _get_supported_distros(dependency_map)
    distro = _recognise_distro(supported_distros)
    if(verbose):
        if(not distro):
            Colour.print('unrecognised distro, please contact srbcheema2@gmail.com for support', Colour.RED)
        else:
            Colour.print('Distro detected to be '+distro+' based',Colour.GREEN)

    all_installed = True

    for d in dependency_map.keys():
        if is_installed(d):
            continue
        rules = dependency_map[d]
        if distro and distro in rules.keys():
            Colour.print('installing '+d+' dependency',Colour.GREEN)
            os.system(rules[distro])
            if not is_installed(d):
                Colour.print('please install ' +d+ ' dependency manually',Colour.YELLOW)
                Colour.print('try command : '+rules[distro],Colour.YELLOW)
                all_installed = False
        else:
            Colour.print('Please install ' +d+ ' dependency manually',Colour.YELLOW)
            all_installed = False

    return all_installed

def remove_dependencies(dependency_map, verbose = False):
    supported_distros = _get_supported_distros(dependency_map)
    distro = _recognise_distro(supported_distros)
    if(verbose):
        if(not distro):
            Colour.print('unrecognised distro, please contact srbcheema2@gmail.com for support', Colour.RED)
        else:
            Colour.print('Distro detected to be '+distro+' based',Colour.GREEN)

    all_removed = True

    for d in dependency_map.keys():
        if not is_installed(d):
            continue
        rules = dependency_map[d]
        if distro and distro in rules.keys():
            Colour.print('removing '+d+' dependency',Colour.GREEN)
            os.system(rules[distro])
            if is_installed(d):
                Colour.print('please remove ' +d+ ' dependency manually',Colour.YELLOW)
                Colour.print('try command : '+rules[distro],Colour.YELLOW)
                all_removed = False
        else:
            Colour.print('Please remove ' +d+' dependency manually',Colour.YELLOW)
            all_removed = False

    return all_removed

def install_dependencies_pkg(dependency_map, verbose=False):
    all_installed = True
    for dependency in dependency_map.keys():
        if is_installed(dependency):
            if verbose: Colour.print('.:Dependency '+dependency+' already installed...',Colour.GREEN)
            continue

        rules = dependency_map[dependency]
        installed_package_managers = _get_installed_package_mangers(rules.keys())

        if len(installed_package_managers) == 0:
            Colour.print('No supported package manager available for ' +Colour.END+ dependency +Colour.RED
                    + ' please contact srbcheema2@gmail.com for support', Colour.RED)
            continue

        Colour.print('.:Installing '+dependency+' dependency',Colour.GREEN)
        for ipm in installed_package_managers :
            os.system(rules[ipm])
            if is_installed(dependency) :# else try other package managers
                break
        if not is_installed(dependency):
            Colour.print('please install ' +Colour.END+ dependency +Colour.YELLOW+ ' manually',Colour.YELLOW)
            for ipm in installed_package_managers :
                Colour.print('try command : '+Colour.END+ rules[ipm],Colour.YELLOW)
            all_installed = False
    return all_installed

def remove_dependencies_pkg(dependency_map, verbose=False):
    all_removed = True
    for dependency in dependency_map.keys():
        if not is_installed(dependency):
            if verbose: Colour.print('.:Dependency '+dependency+' already not installed...',Colour.GREEN)
            continue

        rules = dependency_map[dependency]
        installed_package_managers = _get_installed_package_mangers(rules.keys())

        if len(installed_package_managers) == 0:
            Colour.print('No supported package manager rule available for ' +Colour.END+ dependency + Colour.RED
                    + ' please contact srbcheema2@gmail.com for support', Colour.RED)
            continue

        Colour.print('.:Uninstalling '+dependency+' dependency',Colour.GREEN)
        for ipm in installed_package_managers :
            os.system(rules[ipm])
            if is_installed(dependency) :# else try other package managers
                break
        if not is_installed(dependency):
            Colour.print('please uninstall ' +Colour.END+ dependency +Colour.YELLOW+ ' manually',Colour.YELLOW)
            for ipm in installed_package_managers :
                Colour.print('try command : '+Colour.END+ rules[ipm],Colour.YELLOW)
            all_removed = False
    return all_removed



if __name__ == '__main__':
    dependency_map = {
        'register-python-argcomplete':{
            'ubuntu':'sudo apt remove python-argcomplete',
        },
        'figlet':{
            'ubuntu':'sudo apt remove figlet',
        },
    }
    remove_dependencies(dependency_map,verbose=True)
    dependency_map = {
        'register-python-argcomplete':{
            'ubuntu':'sudo apt install python-argcomplete',
        },
        'figlet':{
            'ubuntu':'sudo apt install figlet',
        },
    }
    install_dependencies(dependency_map,verbose=True)
    install_arg_complete('demo_app')

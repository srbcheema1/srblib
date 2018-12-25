import pytest
import os

from srblib import on_travis, is_installed
from srblib import install_dependencies, remove_dependencies
from srblib import install_dependencies_pkg, remove_dependencies_pkg

def test_install_remove_dependency_using_package_manager_map():
    if(not on_travis):
        return
    assert(is_installed('figlet')==False)

    dependency_map = {
        'figlet':{
            'apt':'sudo apt install -y figlet',
        },
    }
    install_dependencies_pkg(dependency_map,verbose=True)
    assert(is_installed('figlet')==True)

    os.system('figlet test_figlet')

    dependency_map = {
        'figlet':{
            'apt':'sudo apt remove -y figlet',
        },
    }
    remove_dependencies_pkg(dependency_map,verbose=True)
    assert(is_installed('figlet')==False)

def test_install_remove_dependency_legacy():
    if(not on_travis):
        return
    assert(is_installed('figlet')==False)

    dependency_map = {
        'figlet':{
            'ubuntu':'sudo apt install -y figlet',
        },
    }
    install_dependencies(dependency_map,verbose=True)
    assert(is_installed('figlet')==True)

    os.system('figlet test_figlet')

    dependency_map = {
        'figlet':{
            'ubuntu':'sudo apt remove -y figlet',
        },
    }
    remove_dependencies(dependency_map,verbose=True)
    assert(is_installed('figlet')==False)

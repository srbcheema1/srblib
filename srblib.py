from srblib import *

if __name__ == "__main__":
    dependency_map = {
        'figlet':{
            'ubuntu':'sudo apt remove figlet',
        },
    }
    remove_dependencies(dependency_map,verbose=True)
    dependency_map = {
        'figlet':{
            'ubuntu':'sudo apt install figlet',
        },
    }
    # install_dependencies(dependency_map,verbose=True)

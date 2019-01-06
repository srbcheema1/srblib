import os
import shutil
from importlib.util import spec_from_file_location, module_from_spec

from .path import abs_path
from .files import verify_file

# ignore_var_list = ['__class__','__weakref__','__dir__']
class Module:
    def __init__(self,file_path,backup=None):
        '''
        backup should be absolute_path_of_that_file
        '''
        file_path = abs_path(file_path)
        if(not os.path.isfile(file_path)):
            if(not backup): raise('File doesnot exist please provide backup')
            backup = abs_path(backup)
            verify_file(file_path)
            shutil.copy(backup,file_path)

        mod_name = file_path.split('/')[-1].split('.')[0]
        spec = spec_from_file_location(mod_name,file_path)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)

        list_vars = dir(module)
        for var in list_vars:
            # if var not in ignore_var_list:
            setattr(self,var,getattr(module,var))


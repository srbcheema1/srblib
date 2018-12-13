__version__ = '0.0.1'
__mod_name__ = 'srblib'

from .path import abs_path
from .path import is_child_of

from .colour import Colour

from .dependency import install_arg_complete
from .dependency import install_dependencies
from .dependency import is_installed
from .dependency import remove_dependencies

from .files import verify_file
from .files import verify_folder
from .files import remove


from .srb_bank import srbbank
from .srb_json import srbjson

'''
return windows, linux or mac
'''
from .system import get_os_name

from .util import show_dependency_error_and_exit

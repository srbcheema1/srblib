__version__ = '0.0.1'
__mod_name__ = 'srblib'


from .colour import Colour

from .debugger import on_srbpc
from .debugger import on_travis

from .dependency import install_arg_complete
from .dependency import install_dependencies
from .dependency import install_dependencies_pkg
from .dependency import is_installed
from .dependency import remove_dependencies
from .dependency import remove_dependencies_pkg

from .files import file_extension
from .files import file_name
from .files import remove
from .files import verify_file
from .files import verify_folder

# one cant declare more attributes in frozen class
from .frozen import FrozenClass

from .path import abs_path
from .path import is_child_of
from .path import parent_dir
from .path import relative_path

from .srb_bank import srbbank
from .srb_json import srbjson

'''
return windows, linux or mac
'''
from .system import get_os_name

from .util import line_adder
from .util import show_dependency_error_and_exit


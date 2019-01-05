import sys

try:
    import argparse
    from argcomplete import autocomplete
except:
    from .util import show_dependency_error_and_exit
    show_dependency_error_and_exit()

from . import __mod_name__,__version__
from .debugger import _debug_json
from .colour import Colour

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version",
                        action='store_true',
                        help="Display version number")
    parser.add_argument("-d", "--debug",
                        action='store_true',
                        help="Toggle value of debug variable")
    autocomplete(parser)
    parsed_args = parser.parse_args()
    if(parsed_args.version):
        print(__mod_name__+'=='+__version__)
        sys.exit()
    if(parsed_args.debug):
        _debug_json['debug'] = not _debug_json['debug']
        Colour.print('debug value set to: ' + str(_debug_json['debug']), Colour.GREEN)
    print(__file__)


if __name__ == '__main__':
    main()

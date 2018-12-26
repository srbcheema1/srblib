import sys

try:
    import argparse
    from argcomplete import autocomplete
except:
    from .util import show_dependency_error_and_exit
    show_dependency_error_and_exit()

from . import __mod_name__,__version__

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version",
                        action='store_true',
                        help="Display version number")
    autocomplete(parser)
    parsed_args = parser.parse_args()
    if(parsed_args.version):
        print(__mod_name__+'=='+__version__)
        sys.exit()
    return


if __name__ == '__main__':
    main()

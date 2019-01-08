import platform
import sys

def _get_os_name():
    os_name = platform.system().lower()
    if 'window' in os_name:
        return 'windows'
    if 'darwin' in os_name:
        return 'mac'
    if 'linux' in os_name:
        return 'linux'
    return None

ok = _get_os_name() != 'windows'

class Colour:
    BOLD = '\033[1m' if ok else ''
    UNDERLINE = '\033[4m' if ok else ''
    END = '\033[0m' if ok else ''

    GRAY = '\033[90m' if ok else ''
    RED = '\033[91m' if ok else ''
    GREEN = '\033[92m' if ok else ''
    YELLOW = '\033[93m' if ok else ''
    BLUE = '\033[94m' if ok else ''
    PURPLE = '\033[95m' if ok else ''
    CYAN = '\033[96m' if ok else ''
    WHITE = '\033[97m' if ok else ''

    DARKGRAY = '\033[30m' if ok else ''
    DARKRED = '\033[31m' if ok else ''
    DARKGREEN = '\033[32m' if ok else ''
    DARKYELLOW = '\033[33m' if ok else ''
    DARKBLUE = '\033[34m' if ok else ''
    DARKPURPLE = '\033[35m' if ok else ''
    DARKCYAN = '\033[36m' if ok else ''
    DARKWHITE = '\033[37m' if ok else ''

    FULLDARKGRAY = '\033[40m' if ok else ''
    FULLDARKRED = '\033[41m' if ok else ''
    FULLDARKGREEN = '\033[42m' if ok else ''
    FULLDARKYELLOW = '\033[43m' if ok else ''
    FULLDARKBLUE = '\033[44m' if ok else ''
    FULLDARKPURPLE = '\033[45m' if ok else ''
    FULLDARKCYAN = '\033[46m' if ok else ''
    FULLDARKWHITE = '\033[47m' if ok else ''

    FULLGRAY = '\033[100m' if ok else ''
    FULLRED = '\033[101m' if ok else ''
    FULLGREEN = '\033[102m' if ok else ''
    FULLYELLOW = '\033[103m' if ok else ''
    FULLBLUE = '\033[104m' if ok else ''
    FULLPURPLE = '\033[105m' if ok else ''
    FULLCYAN = '\033[106m' if ok else ''
    FULLWHITE = '\033[107m' if ok else ''


    def print(message,colour='',end='\n'):
        os_name = _get_os_name()
        end_colour = Colour.END
        if(os_name == 'windows'):
            colour = ''
            end_colour = ''
        # print(colour + message + end_colour,end=end)
        sys.stderr.write(colour + message + end_colour + end)


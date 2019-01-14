import platform

def get_os_name():
    os_name = platform.system().lower()
    if 'window' in os_name:
        return 'windows'
    if 'darwin' in os_name:
        return 'mac'
    if 'linux' in os_name:
        return 'linux'
    return None

os_name = get_os_name()

on_windows = False
if os_name == 'windows':
    on_windows = True

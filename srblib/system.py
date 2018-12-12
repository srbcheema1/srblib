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

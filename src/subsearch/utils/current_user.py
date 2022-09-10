import socket
import sys
import winreg as reg

COMPUTER_NAME = socket.gethostname()


def got_key() -> bool:
    """
    Check if current user has the registry key subsearch for the context menu

    Returns:
        bool: True if key exists, False if key does not exist
    """
    sub_key = r"Software\Classes\*\shell\0.subsearch\command"
    try:
        with reg.ConnectRegistry(None, reg.HKEY_CURRENT_USER) as hkey:
            reg.OpenKey(hkey, sub_key)
            return True
    except Exception:
        return False


def check_is_exe() -> bool:
    if sys.argv[0].endswith(".exe"):
        return True
    return False

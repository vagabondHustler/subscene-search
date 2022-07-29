import os
import socket
import sys
import winreg

from src.utilities.local_paths import root_directory
from src.utilities.current_user import is_exe_version

COMPUTER_NAME = socket.gethostname()

# write value to "Icon"
def context_menu_icon():
    from src.utilities.read_config_json import get

    use: str = get("cm_icon")
    ss_path = "Software\Classes\Directory\Background\shell\SubSearch"
    icon_path = root_directory("data", "16.ico")
    with winreg.ConnectRegistry(COMPUTER_NAME, winreg.HKEY_CURRENT_USER) as hkey:
        with winreg.OpenKey(hkey, ss_path, 0, winreg.KEY_WRITE) as subkey_ss:
            if use == "True":
                winreg.SetValueEx(subkey_ss, "Icon", 0, winreg.REG_SZ, icon_path)
            if use == "False":
                winreg.SetValueEx(subkey_ss, "Icon", 0, winreg.REG_SZ, "")


# write value to (Default)
def write_command_subkey():
    from src.utilities.read_config_json import get

    focus = get("terminal_focus")

    command_path = "Software\Classes\Directory\Background\shell\SubSearch\command"
    if is_exe_version():
        exe_path = root_directory(file_name="SubSearch.exe")
    else:
        ppath = os.path.dirname(sys.executable)
        set_title = "import ctypes; ctypes.windll.kernel32.SetConsoleTitleW('SubSearch');"
        set_wd = f"import os; working_path = os.getcwd(); os.chdir('{root_directory()}');"
        run_main = "import main; os.chdir(working_path); main.main()"

        tfocus = f'{ppath}\python.exe -c "{set_title} {set_wd} {run_main}"'
        tsilent = f'{ppath}\pythonw.exe -c "{set_title} {set_wd} {run_main}"'

    with winreg.ConnectRegistry(COMPUTER_NAME, winreg.HKEY_CURRENT_USER) as hkey:
        with winreg.OpenKey(hkey, command_path, 0, winreg.KEY_WRITE) as subkey_command:
            if is_exe_version():
                winreg.SetValueEx(subkey_command, "", 0, winreg.REG_SZ, exe_path)
                return
            if focus == "True":
                winreg.SetValueEx(subkey_command, "", 0, winreg.REG_SZ, tfocus)
                return
            if focus == "False":
                winreg.SetValueEx(subkey_command, "", 0, winreg.REG_SZ, tsilent)
                return


def restore_context_menu():
    regkey = root_directory("data", "regkey.reg")
    os.system(f'cmd /c "reg import "{regkey}"')
    context_menu_icon()
    write_command_subkey()


def remove_context_menu():
    shell_path = "Software\Classes\Directory\Background\shell"
    ss_path = "Software\Classes\Directory\Background\shell\SubSearch"

    with winreg.ConnectRegistry(COMPUTER_NAME, winreg.HKEY_CURRENT_USER) as hkey:
        with winreg.OpenKey(hkey, ss_path, 0, winreg.KEY_WRITE) as ss_key:
            winreg.DeleteKey(ss_key, "command")

    with winreg.ConnectRegistry(COMPUTER_NAME, winreg.HKEY_CURRENT_USER) as hkey:
        with winreg.OpenKey(hkey, shell_path, 0, winreg.KEY_WRITE) as shell_key:
            winreg.DeleteKey(shell_key, "SubSearch")


# imports empty registry key to be filled in with values later
def add_context_menu():
    regkey = root_directory("data", "regkey.reg")
    os.system(f'cmd /c "reg import "{regkey}"')
    context_menu_icon()
    write_command_subkey()

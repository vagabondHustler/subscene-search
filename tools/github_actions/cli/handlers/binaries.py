import hashlib
import importlib
import socket
import subprocess
import time
import winreg
from pathlib import Path
from typing import Any

from tools.github_actions.cli.globals import (
    CONFIG_TOML_PATH,
    LOG_LOG_PATH,
    ARTIFACTS_PATH,
    EXE_FREEZE_PATH,
    EXE_INSTALLED_PATH,
    HASHES_PATH,
    MSI_FREEZE_PATH,
    STYLE_SEPERATOR,
)
from tools.github_actions.cli.handlers import github_actions, io_python, log
from tools.github_actions.cli import install_module


def test_msi_package(name: str, msi_package_path: Path) -> None:
    _app_version = io_python.read_string()
    installer_action = {"install": "/i", "uninstall": "/x"}.get(name, None)
    log.verbose_print(f"MSI Package is {name}ing Subsearch {_app_version}")
    command = ["msiexec.exe", installer_action, msi_package_path, "/norestart", "/quiet"]
    subprocess.run(command, check=True)  # type: ignore
    log.verbose_print(f"{name.capitalize()} completed")


def list_files_in_directory(directory: Path):
    try:
        files = list(directory.glob("*"))
        for file in files:
            log.verbose_print(file)
    except FileNotFoundError:
        log.verbose_print(f"The directory {directory} does not exist.")
    except PermissionError:
        log.verbose_print(f"Permission error accessing {directory}.")
    except Exception as e:
        log.verbose_print(f"An error occurred: {e}")


def is_process_running(psutil, process_name) -> bool:
    for process in psutil.process_iter(["pid", "name"]):
        if process.info["name"].lower() == process_name.lower():
            return True
    return False


def wait_for_process(psutil, process_name: str, test_length: int) -> int:
    for duration in range(test_length + 1):
        if not is_process_running(psutil, process_name):
            return duration
        time.sleep(1)
    return duration


def end_process(psutil, process_name: str) -> None:
    for process in psutil.process_iter(["pid", "name"]):
        if process.info["name"].lower() == process_name.lower():
            log.verbose_print(f"Terminating {process_name}")
            process.terminate()


def expected_files_exists():
    expected_files: list[Path] = [LOG_LOG_PATH, CONFIG_TOML_PATH]
    for i in expected_files:
        if not i.parent.exists():
            raise FileNotFoundError(f"Directory '{i}' does not exist.")
        if not i.is_file():
            raise FileNotFoundError(f"File '{i}' does not exist.")


def test_executable(test_length: int = 10) -> None:
    psutil = install_module._psutil()
    process_name = EXE_INSTALLED_PATH.name
    log.verbose_print(f"{process_name} has been initiated for testing")
    subprocess.Popen([EXE_INSTALLED_PATH.as_posix()])
    log.verbose_print(f"Waiting {test_length} seconds for process...")
    duration = wait_for_process(psutil, process_name, test_length)
    expected_files_exists()
    log.verbose_print(f"{process_name} created expected files")
    log.verbose_print(f"{process_name} ran for the expected {test_length} seconds")
    if duration < test_length:
        raise RuntimeError(f"{process_name} did not run for the expected duration")
    end_process(psutil, process_name)


def registry_key_exists() -> bool:
    try:
        with winreg.ConnectRegistry(socket.gethostname(), winreg.HKEY_CURRENT_USER) as hkey:
            winreg.OpenKey(hkey, r"Software\Classes\*\shell\Subsearch", 0, winreg.KEY_WRITE)
            return True
    except FileNotFoundError:
        return False


def _software_test_result(name: str, result: str) -> None:
    summary = f"Exe exists: {EXE_INSTALLED_PATH.is_file()}, Log exists: {LOG_LOG_PATH.is_file()}, Config exists: {CONFIG_TOML_PATH.is_file()}, Registry key exists: {registry_key_exists()}"
    github_actions.set_step_summary(f"After {name} test:")
    github_actions.set_step_summary(summary.replace(",", "\n"))
    github_actions.set_step_summary(f"Test {result}\n")
    print(f"")
    log.verbose_print(f"{summary}")
    log.verbose_print(f"{name.capitalize()} {result}")
    print(f"{STYLE_SEPERATOR}")


def set_test_result(name: str) -> None:
    tests = {
        "install": EXE_INSTALLED_PATH.is_file() and registry_key_exists(),
        "executable": LOG_LOG_PATH.is_file() and CONFIG_TOML_PATH.is_file(),
        "uninstall": not EXE_INSTALLED_PATH.is_file() and not registry_key_exists(),
    }
    if tests[name]:
        _software_test_result(name, "passed")
    else:
        list_files_in_directory(EXE_INSTALLED_PATH.parent)
        list_files_in_directory(LOG_LOG_PATH.parent)
        _software_test_result(name, "failed")
        raise RuntimeError(f"{name} test failed")


def calculate_sha256(file_path: str) -> str:
    sha256_hash = hashlib.sha256()
    _file_path = Path(file_path)
    if not Path(_file_path).is_file():
        raise FileNotFoundError(f"No file found at {_file_path}")

    with open(_file_path, "rb") as file:
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def create_hashes_file(**kwargs: dict[str, Any]) -> None:
    hashes_path = kwargs.get("hashes_path", HASHES_PATH)
    if not ARTIFACTS_PATH.is_dir():
        ARTIFACTS_PATH.mkdir(parents=True, exist_ok=True)
    with open(hashes_path, "w") as f:  # type: ignore
        log.verbose_print(f"Created file: {hashes_path}")
        pass


def prepare_build_artifacts():
    log.verbose_print(f"Collecting files")
    files = [MSI_FREEZE_PATH, EXE_FREEZE_PATH]
    for file in files:
        file.replace(ARTIFACTS_PATH / file.name)
        log.verbose_print(f"{file.name} moved to ./artifacts")


def write_to_hashes(**kwargs: dict[str, Any]) -> None:
    log.verbose_print(f"Collectiong hashes")
    lines: dict[int, str] = {}
    file_paths: list[Path] = kwargs.get("hashes_path", [MSI_FREEZE_PATH, EXE_FREEZE_PATH])  # type: ignore
    hashes_path: Path = kwargs.get("hashes_path", HASHES_PATH)  # type: ignore

    if not hashes_path.is_file():
        create_hashes_file(hashes_path=hashes_path)  # type: ignore

    for enum, file_path in enumerate(file_paths):
        sha256 = calculate_sha256(file_path)  # type: ignore
        file_name = f"{file_path.name}"
        lines[enum] = f"{sha256} *{file_name}\n"
        log.verbose_print(f"Setting new Github Action output")
        log.verbose_print(f"{file_path.suffix[1:]}_hash={sha256}")
        github_actions.set_step_output(name=f"{file_path.suffix[1:]}_hash", value=f"{sha256}")
        github_actions.set_step_summary(f"{file_name}: {sha256}")

    with open(hashes_path, "a") as file:
        log.verbose_print(f"Writing to {hashes_path.name}")
        file.writelines(lines.values())

    [log.verbose_print(f"Wrote {i} to file") for i in lines.values()]  # type: ignore

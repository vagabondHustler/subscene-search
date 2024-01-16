import dataclasses
import logging
from pathlib import Path
import threading
from typing import Optional, TypeVar

from subsearch.globals import metaclasses
from subsearch.globals.constants import FILE_PATHS

DATACLASS = TypeVar("DATACLASS")


class ANSIEscapeSequences:
    """
    ANSI escape sequences for text colors
    """

    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class LogMessage:
    DONE_WITH_TASKS = dict(
        message="Done with task",
        level="info",
        hex_color="#89b4fa",
        end_new_line=True,
    )


class Logger(metaclass=metaclasses.Singleton):
    def __init__(self, *args, **kwargs) -> None:
        self.logger_name = kwargs.get("logger_name", "subsearch")
        self.log_file_path = kwargs.get("debug_log_file", FILE_PATHS.log)
        self.datefmt = kwargs.get("datefmt", "%d-%b-%y %H:%M:%S")
        self.txtfmt = kwargs.get("txtfmt" "%(asctime)s - %(levelname)s - %(message)s")
        self._debug_logger = self.create_logger()
        self._lock = threading.Lock()
        self._ansi = ANSIEscapeSequences

    def create_logger(self) -> logging.Logger:
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler(self.log_file_path, mode="w")
        file_handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter(self.txtfmt, datefmt=self.datefmt)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

    def log(self, message: str, **kwargs) -> None:
        with self._lock:
            self._log(message, **kwargs)
            self._print(message, **kwargs)

    def _log(self, message: str, **kwargs) -> None:
        level = kwargs.get("level", "info")
        log_methods = {
            "debug": self._debug_logger.debug,
            "info": self._debug_logger.info,
            "warning": self._debug_logger.warning,
            "error": self._debug_logger.error,
            "critical": self._debug_logger.critical,
        }

        log_methods[level](message)

    def _print(self, message, **kwargs) -> None:
        print_allowed = kwargs.get("print_allowed", True)
        hex_color = kwargs.get("hex_color", "#")
        style = kwargs.get("style", "")

        if not print_allowed:
            pass
        elif hex_color == "#" and len(hex_color) == 1:
            print(message)
        elif hex_color.startswith("#") and len(hex_color[1:]) == 6:
            self._color_print(message, hex_color, style)

    def _hex_to_ansi(self, hex_color: str) -> str:
        r, g, b = int(hex_color[1:3], 16), int(hex_color[3:5], 16), int(hex_color[5:7], 16)
        return f"\033[38;2;{r};{g};{b}m"

    def _color_print(self, message: str, hex_color: str, style: str) -> None:
        color_code = self._hex_to_ansi(hex_color)
        style_code = getattr(self._ansi, style.upper()) if style != "" else ""
        print(f"{style_code}{color_code}{message}{self._ansi.RESET}")


def stdout(message: str, **kwargs) -> None:
    end_new_line = kwargs.get("end_new_line", False)
    _logger = Logger()
    _logger.log(message, **kwargs)
    if end_new_line:
        _logger.log("", **kwargs)


def stdout_in_brackets(message: str, **kwargs) -> None:
    stdout(f"--- [{message}] ---", hex_color="#fab387", style="bold", **kwargs)


def stdout_match(provider: str, subtitle_name: str, result: int, threshold: int, **kwargs) -> None:
    if result >= threshold:
        stdout(f"> {provider:<14}{result:>3}% {subtitle_name}", hex_color="#a6e3a1")
    else:
        stdout(f"  {provider:<14}{result:>3}% {subtitle_name}")


def stdout_path_action(action_type: str, src: Path, dst: Optional[Path] = None, **kwargs) -> None:
    if src.is_file():
        type_ = "file"
    elif src.is_dir():
        type_ = "directory"
    else:
        return None

    __src = src.relative_to(src.parent.parent) if src else None
    __dst = dst.relative_to(dst.parent.parent) if dst else None

    action_messages = {
        "remove": rf"Removing {type_}: ...\{__src}",
        "rename": rf"Renaming {type_}: ...\{__src} -> ...\{__dst}",
        "move": rf"Moving {type_}: ...\{__src} -> ...\{__dst}",
        "extract": rf"Extracting archive: ...\{__src} -> ...\{__dst}",
    }

    message = action_messages.get(action_type)

    if not message:
        raise ValueError("Invalid action type")

    stdout(message, **kwargs)


def stdout_dataclass(instance: DATACLASS, **kwargs) -> None:
    if not dataclasses.is_dataclass(instance):
        raise ValueError("Input is not a dataclass instance.")
    stdout_in_brackets(instance.__class__.__name__, **kwargs)
    for field in dataclasses.fields(instance):
        key = field.name
        value = getattr(instance, key)
        padding = " " * (30 - len(key))
        stdout(f"{key}:{padding}{value}", **kwargs)

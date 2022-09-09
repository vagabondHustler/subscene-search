from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Window:
    """
    Class for storing settings for window size.
    """

    width: int = 738
    height: int = 720


@dataclass(frozen=True, order=True)
class Color:
    """
    Class for storing colors for widgets.
    """

    purple: str = "#b294bb"
    red: str = "#bc473b"
    dark_red: str = "#89332a"
    red_brown: str = "#b26947"
    orange: str = "#ab7149"
    light_orange: str = "#de935f"
    yellow: str = "#f0c674"
    blue: str = "#81a2be"
    cyan: str = "#82b3ac"
    green: str = "#9fa65d"
    green_brown: str = "#a59256"
    grey: str = "#4c4c4c"
    light_grey: str = "#727272"
    silver_grey: str = "#8a8a8a"
    white_grey: str = "#bdbdbd"
    dark_grey: str = "#1a1b1b"
    mid_grey_black: str = "#111111"
    light_black: str = "#0e0e0e"
    black: str = "#151515"
    dark_black: str = "#000000"


@dataclass(frozen=True, order=True)
class Font:
    """
    Class for storing fonts for widgets
    """

    cas6b: str = "Cascadia 6 bold"
    cas8: str = "Cascadia 8"
    cas8i: str = "Cascadia 8 italic"
    cas8b: str = "Cascadia 8 bold"
    cas10b: str = "Cascadia 10 bold"
    cas11: str = "Cascadia 11"
    cas20b: str = "Cascadia 20 bold"

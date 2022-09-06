from pathlib import Path

inited = False
root = None


def init(func):
    def wrapper(*args, **kwargs):
        global inited
        global root

        if not inited:
            from tkinter import _default_root

            path = (Path(__file__).parent / "sun-valley.tcl").resolve()

            try:
                _default_root.tk.call("source", str(path))
            except AttributeError:
                raise RuntimeError(
                    "can't set theme. Tk is not initialized. "
                    + "Please first create a tkinter.Tk instance, then set the theme."
                ) from None
            else:
                inited = True
                root = _default_root

        return func(*args, **kwargs)

    return wrapper


@init
def set_theme(theme):
    if theme not in {"grey"}:
        raise RuntimeError(f"not a valid theme name: {theme}")

    root.tk.call("set_theme", theme)


@init
def get_theme():
    theme = root.tk.call("ttk::style", "theme", "use")

    try:
        return {"sun-valley-dark": "grey"}[theme]
    except KeyError:
        return theme


@init
def toggle_theme():
    if get_theme() == "grey":
        use_grey_theme()
    else:
        use_grey_theme()


use_grey_theme = lambda: set_theme("grey")
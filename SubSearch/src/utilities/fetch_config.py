from src.utilities.local_paths import root_directory
from src.utilities.fetch_parameters import read_data


# get said value(s) from config.json
def get(output):
    config_json = read_data(root_directory("data", "config.json"))

    def language() -> str:
        language = config_json.language
        lang, lang_abbr = language.split(", ")
        return lang, lang_abbr

    def languages() -> list:
        ls = config_json.languages
        return ls

    def video_ext() -> list:
        voe = config_json.video_ext
        return voe

    def precent() -> int:
        p = config_json.percentage_pass
        return p

    def terminal_focus() -> str:
        tf = config_json.terminal_focus
        return tf

    def hearing_impaired() -> str:
        hi = config_json.hearing_impaired
        return hi

    def cm_icon() -> str:
        cm = config_json.context_menu_icon
        return cm

    if output == "language":
        return language()
    if output == "languages":
        return languages()
    if output == "video_ext":
        return video_ext()
    if output == "percentage":
        return precent()
    if output == "terminal_focus":
        return terminal_focus()
    if output == "hearing_impaired":
        return hearing_impaired()
    if output == "cm_icon":
        return cm_icon()

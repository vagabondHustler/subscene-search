import json
from dataclasses import dataclass

from num2words import num2words


@dataclass
class ConfigData:
    language: str
    hearing_impaired: str
    languages: list[str]
    video_ext: list
    percentage_pass: int
    terminal_focus: str
    context_menu_icon: str


@dataclass
class SearchParameters:
    url_subscene: str
    url_opensubtitles: str
    title: str
    year: int
    season: str
    season_ordinal: str
    episode: str
    episode_ordinal: str
    tv_series: bool
    release: str
    group: str
    file_hash: str


def read_data(config_file: str) -> ConfigData:
    with open(config_file, encoding="utf-8") as file:
        data = json.load(file)
        return ConfigData(**data)


def split_last_hyphen(string: str) -> str:
    group = string.rsplit("-", 1)[-1]
    return group


def get_parameters(dir_path, lang_abbr, file_hash, file_name) -> SearchParameters:
    # default values
    _title = None
    year = "N/A"
    season = "N/A"
    season_ordinal = "N/A"
    episode = "N/A"
    episode_ordinal = "N/A"
    group = "N/A"
    tv_series = False
    year_found = False

    # if no file is found use the current directory path
    if file_name is None:
        release = dir_path.split("\\")[-1]
    else:
        release = file_name

    # find season, episode, make it ordinal and set tv_series to true if it is a tv-series
    for item in release.lower().split("."):
        if item.startswith("s") and item[-1].isdigit() and "e" in item:
            season, episode = item.replace("s", "").replace("e", " ").split(" ")
            season_ordinal = num2words(int(season), lang=lang_abbr, to="ordinal")
            episode_ordinal = num2words(int(episode), lang=lang_abbr, to="ordinal")
            if season[-1].isdigit():
                tv_series = True
                break

    string_list = release.lower().split(".")
    subtract = []
    # list is reversed if a year is apart of the title, like "2001: A Foo Bar" from 1991
    # this is to prevent the year from the title being used as the release year of the movie/show
    for item in string_list[::-1]:
        # if year is found everything else in the list should be the release name
        if year_found or item.startswith("s") and item[-1].isdigit():
            _title = (i for i in string_list if i not in subtract)
            break
        if item.isdigit() and len(item) == 4:
            year_found = True
            year = item
        subtract.append(item)

    if _title is not None:
        title = " ".join(x for x in _title)
    else:
        title = release

    if "-" in release:
        group = split_last_hyphen(release)

    subscene = "https://subscene.com/subtitles/searchbytitle?query="
    opensubtitles = "https://www.opensubtitles.org/en/search/sublanguageid-eng/moviename-"
    url_subscene = f"{subscene}{title}".replace(" ", "%20")
    url_opensubtitles = f"{opensubtitles}{file_hash}"

    parameters = {
        "url_subscene": url_subscene,
        "url_opensubtitles": url_opensubtitles,
        "title": title,
        "year": year,
        "season": season,
        "season_ordinal": season_ordinal,
        "episode": episode,
        "episode_ordinal": episode_ordinal,
        "tv_series": tv_series,
        "release": release,
        "group": group,
        "file_hash": file_hash,
    }
    return SearchParameters(**parameters)

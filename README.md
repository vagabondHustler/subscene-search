<div align="center">

![prtsc0](https://github.com/vagabondHustler/SubSearch/blob/main/assets/subsearch_transparent.png)

![Status](https://img.shields.io/badge/status-active-success?color=9fa65d&style=flat-square)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/vagabondhustler/subsearch?color=c49b5d&style=flat-square)
![Version](https://img.shields.io/github/v/release/vagabondHustler/SubSearch?color=de935e&display_name=tag&include_prereleases&style=flat-square)
![Downloads](https://img.shields.io/github/downloads/vagabondHustler/SubSearch/total?color=ba9888&style=flat-square)
![License](https://img.shields.io/github/license/vagabondhustler/SUbSearch?color=82a2bd&style=flat-square)

</div>

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started_src)
- [Preview](#preview)
- [Source](#src)
- [Executable](#exe)
- [Supported Languages](#lsupport)
- [Other Languages](#notsupport)
- [Authors](#authors)
- [Contributing](https://github.com/vagabondHustler/SubSearch/blob/main/CONTRIBUTING.md)
- [Reporting a Vulnerability](https://github.com/vagabondHustler/SubSearch/blob/main/SECURITY.md)

## About <a name = "about"></a>

Download subtitles for movies and tv-series, automatically for well known scene groups with two easy mouse clicks inside the directory containing the video file, if there is no video file inside the directory, the directory name will be used as a search parameter.

Made mainly to learn python and git, by doing. There are probably better repositories out there that grab subtitles automatically from the web. But feel free to check this one out if you want to. The average run time is around 1 second, a little bit longer for TV-Series due to the high amount of titles.

## Preview <a name = "preview"></a>

<div align="center">

What it looks like while searching for subs if show terminal is disabled

![prtsc1](https://github.com/vagabondHustler/SubSearch/blob/main/assets/preview.gif)

What the settings menu looks like and available options

![prtsc2](https://github.com/vagabondHustler/SubSearch/blob/main/assets/gui_21018.png)

What the download window looks like with subtitles that were not downloaded

![prtsc2](https://github.com/vagabondHustler/SubSearch/blob/main/assets/gui_dlw_2918.png)

</div>

## Getting Started <a name = "getting_started_src"></a>

Source is probably faster than the executable version, but the executable can be run without installing a Python interpreter or any modules.

### Source <a name = "src"></a>

Download Python 3.10 - [Download URL](https://www.python.org/downloads/)

Download SubScene

`git clone https://github.com/vagabondHustler/SubSearch`

Install dependencies

`pip install -r "https://raw.githubusercontent.com/vagabondHustler/SubSearch/main/docs/requirements.txt"`

Run main.py from where it is located

`python ./SubSearch/main.py`

To access the settings, run main.py again

Right-click inside any folder containing the movie/series and you're done!

If no subtitles are found or no subtitles (including the folder subs with extra .srt files) are synced with the movie check the search.log for a list with download links to all the different subtitles that didn't pass the search threshold percentage or decrease the value in the settings GUI, accessed from main.py

### Executable <a name = "exe"></a>

Download SubSearch-vx.x.x-win-x64.zip from releases - [Download URL](https://github.com/vagabondHustler/SubSearch/releases)

Unzip file and run SubSearch.exe

If you get a PUA message, click `More info`

![prtsc3](https://github.com/vagabondHustler/SubSearch/blob/main/assets/moreinfo.png)

![prtsc4](https://github.com/vagabondHustler/SubSearch/blob/main/assets/runanyway.png)

Right-click inside any folder containing the movie/series and you're done!

If no subtitles are found or no subtitles (including the folder subs with extra .srt files) are synced with the movie check the search.log for a list with download links to all the different subtitles that didn't pass the search threshold percentage or decrease the value in the settings GUI, accessed from SubSearch.exe

## Supported languages <a name = "lsupport"></a>

- Arabic, `ar`
- Brazillian Portuguese, `pt_BR`
- Danish, `dk`
- Dutch, `nl`
- English, `en`
- Finnish, `fi`
- French, `fr`
- German, `de`
- Hebrew, `he`
- Indonesian, `id`
- Italian, `it`
- Korean, `ko`
- Norwegian, `no`
- Romanian, `ro`
- Spanish, `es`
- Swedish, `sv`
- Thai, `th`
- Turkish, `tr`
- Vietnamese, `vi`

## Other languages <a name = "notsupport"></a>

These languages are not tested at all, but should work if u know the [ISO 639-1 code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). These can be entered manually in the settings GUI, in the entry field  `🞂 Enter language here 🞀` and then pressing the button Add, the button `...` brings up this list.

- Albanian, `sq`
- Armenian, `hy`
- Azerbaijani, `az`
- Basque, `eu`
- Belarusian, `be`
- Bosnian, `bs`
- Bulgarian, `bg`
- Bulgarian/ English, `bg_en`
- Burmese, `my`
- Cambodian/Khmer, `km`
- Catalan, `ca`
- Croatian, `hr`
- Czech, `cs`
- Dutch/ English, `nl_en`
- English/ German, `en_de`
- Esperanto, `eo`
- Estonian, `et`
- Georgian, `ka`
- Greenlandic, `kl`
- Hindi, `hi`
- Hungarian, `hu`
- Hungarian/ English, `hu_en`
- Icelandic, `is`
- Japanese, `ja`
- Kannada, `kn`
- Kinyarwanda, `rw`
- Kurdish, `ku`
- Latvian, `lv`
- Lithuanian, `lt`
- Macedonian, `mk`
- Malayalam, `ml`
- Manipuri, `mn`
- Mongolian, `mn`
- Nepali, `ne`
- Pashto, `ps`
- Punjabi, `pa`
- Russian, `ru`
- Serbian, `sr`
- Sinhala, `si`
- Slovak, `sk`
- Slovenian, `sl`
- Somali, `so`
- Sundanese, `su`
- Swahili, `sw`
- Tagalog, `tl`
- Tamil, `ta`
- Telugu, `te`
- Ukrainian, `uk`
- Urdu, `ur`
- Yoruba, `yo`

## Authors <a name = "authors"></a>

- [@vagabondHustler](https://github.com/vagabondHustler)

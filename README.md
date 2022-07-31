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
- [Special Thanks to](#thanks)

## About <a name = "about"></a>

- Automatically search, download and extract subtitles for any movie or show with one easy mouse click from the context menu.
- Has a GUI for all the custom settings that can be configured.
- For 69 different languages, of which 19 are fully supported and tested.
- Can be configured to include hearing impaired subtitles only, none-hearing impaired subtitles only or both.
- Configure how strictly the file name has to match the search results.
- Can be ran from a compiled executable, without the need for a Python interpreter and importing modules.
- Subtitles are gathered from subscene and opensubtitles.

This started as a fun project to learn how to code in python and how to use git, has now developed into a application I use daily and enjoy working on. There are many similar repositories out there that grab subtitles automatically from the web, so this might not be the most unique project. But feel free to check this one out, might offer something new. Have tried to make the setup processes as painless as possible with the use of as few external modules as possible. The average run time is around 1 second, a little bit longer for TV-Series due to the high amount of titles.

Feel free to ask me anything about this project, request new features, contribute or give constructive feedback.

## Preview <a name = "preview"></a>

<div align="center">

What it looks like while searching for subs if show terminal is disabled

![prtsc1](https://github.com/vagabondHustler/SubSearch/blob/main/assets/preview.gif)

What the settings menu looks like and available options

![prtsc2](https://github.com/vagabondHustler/SubSearch/blob/main/assets/gui_21123.png)

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

These languages are not tested at all, but should work if all the [ISO 639-1 code](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) are correct. These languages can be entered manually in the settings GUI, in the entry field  `🞂 Enter language here 🞀` and then pressing the button Add, the button `...` brings up this list.

![other_languages](https://github.com/vagabondHustler/SubSearch/blob/main/assets/other_languages_21123.png)

## Authors <a name = "authors"></a>

- [@vagabondHustler](https://github.com/vagabondHustler)

## Special Thanks to <a name = "thanks"></a>

- [othneildrew](https://github.com/othneildrew/Best-README-Template) for `README` template
- [pimoroni](https://github.com/pimoroni/template-python/blob/master/.github/CONTRIBUTING.md) for `CONTRIBUTING` template
- [manojmj92](https://github.com/manojmj92/subtitle-downloader) for inspiration, ways of solving similar problems

<div align="center">
    
![prtsc0](https://github.com/vagabondHustler/SubSearch/blob/main/assets/subsearch_transparent.png)

![prtsc1](https://github.com/vagabondHustler/SubSearch/blob/main/assets/preview.gif)
![prtsc2](https://github.com/vagabondHustler/SubSearch/blob/main/assets/gui_258.png)

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/vagabondhustler/subsearch)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started_src)
- [Source](#src)
- [Executable](#exe)
- [Language support](#lsupport)
- [Authors](#authors)
- [Misc](#misc)

## About <a name = "about"></a>

Download subtitles for movies and tv-series, automatically for well known scene groups with two easy mouse clicks inside the directory containing the video file, if there is no video file inside the directory, the directory name will be used as a search parameter.

This can be useful if the video file is comppressed inside a rar/zip archive or if the video file is of a unusual extension type not implement in the code.

Made mainly to learn python and git, by doing. There are probably better repositories out there that grab subtitles automatically from the web. But feel free to check this one out if you want to. The avragee run time is around 1 second, a little bit longer for TV-Series due to the high amount of titles, season eppisode to go trough, but not by much if you are searching with a [supported](#lsupport) language.

## Getting Started - Source <a name = "getting_started_src"></a>

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

If no subtitles are found or no subtitles (including the folder subs with extra .srt files) are synced with the movie check the search.log for a list with download links to all the diffrent subtitles that didn't pass the search threshold percentage or decreese the value in the settings GUI, accessed from main.py

### Executable <a name = "exe"></a>

Download SubSearch-vx.x.x-win-x64.zip from releases - [Download URL](https://github.com/vagabondHustler/SubSearch/releases)

Unzip file and run SubSearch.exe

If you get a PUA message, click `More info`

![prtsc3](https://github.com/vagabondHustler/SubSearch/blob/main/assets/moreinfo.png)

![prtsc4](https://github.com/vagabondHustler/SubSearch/blob/main/assets/runanyway.png)

Right-click inside any folder containing the movie/series and you're done!

If no subtitles are found or no subtitles (including the folder subs with extra .srt files) are synced with the movie check the search.log for a list with download links to all the diffrent subtitles that didn't pass the search threshold percentage or decreese the value in the settings GUI, accessed from SubSearch.exe

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

## Authors <a name = "authors"></a>

- [@vagabondHustler](https://github.com/vagabondHustler)

## Misc <a name = "misc"></a>

Registry key can be found here: `Computer\HKEY_CLASSES_ROOT\Directory\Background\shell\SubSearch`

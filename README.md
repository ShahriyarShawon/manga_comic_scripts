# Manga Comic Scripts
---
A bunch of shell scripts I have made to make downloading manga and comics easier. 


## Requirements
```bash
zip
# Make sure you get the python version of html2text
# There is a version on the brew (macos) and apt (debian) repositories
# that aren't the right version
# For Arch you can probably find it by running `yay -Ss html2text`
# everyone else should probably just run `pip install html2text`
# and make sure the path to python scripts is in your PATH
html2text
curl
```

## Installation
Just copy the script you want to use to a directory that is in your path
ex. make a ~/scripts directory or something and make sure it's in your path

```bash
git clone https://github.com/ShahriyarShawon/manga_comic_scripts.git
cd manga_comic_scripts
cp manganelo_downloader manganelo_links ~/Location/Of/Your/Scripts/Folder
```

## Usage 

### manganelo_downloader
used to download single issues of manga
```bash
manganelo_downloader <manganelo chapter link>
# example
manganelo_downloader https://chap.manganelo.com/manga-dn117633/chapter-87
```
manganelo_downloader preserves the directory where all the source images are contained. Delete it manually or contribute a fix.

### manganelo_links
lists all issues of a manga given the mangas root link
using it in a for statement with the `manganelo_downloader`
allows downloading of all issues
```bash
for link in $(manganelo_links <manganelo manga link>);do
    echo $link | manganelo_downloader
done
# example
for link in $(manganelo_links https://chap.manganelo.com/manga-dn117633/);do
    echo $link | manganelo_downloader
done
```
## License MIT

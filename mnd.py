from bs4 import BeautifulSoup as BS
import requests

import sys 
import os
from zipfile import ZipFile
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-f", "--file", help="File with urls of chapters to download"
)
parser.add_argument(
    "-u", "--url", help="URL of chapter to download"
)

def download_chapter(link: str):
    chapter_name = link.split("/")[-1]

    try:
        os.mkdir(chapter_name)
    except FileExistsError:
        print("File already exists, skipping directory creation")

    content = requests.get(link).content
    soup = BS(content, 'html.parser')

    chapter_container = soup.find_all("div", class_="container-chapter-reader")[-1]
    img_tags = chapter_container.find_all("img")
    num_pages = len(img_tags)
    for i in range(num_pages):
        with open("{}/{}.jpg".format(chapter_name, str(i).zfill(3)),"wb") as f:
            image_bytes = requests.get(img_tags[i]["src"]).content
            print("Downloading {}".format(img_tags[i]["src"]))
            f.write(image_bytes)


    with ZipFile("{}.cbz".format(chapter_name), mode="w") as zipfile:
        images = os.listdir(chapter_name)
        images.sort()
        for image in images:
            print("Writing {}".format(image))
            zipfile.write("{}/{}".format(chapter_name, image))




args = parser.parse_args()
if args.file:
    with open(args.file, "r") as input_file:
        links = [link.strip() for link in input_file.readlines() ]
        for link in links:
            download_chapter(link)
else:
    LINK = args.url
    download_chapter(LINK)
    
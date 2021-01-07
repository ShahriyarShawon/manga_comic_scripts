from bs4 import BeautifulSoup as BS
import requests

import sys 


LINK = sys.argv[-1]
manga_id = LINK.split("/")[-1]
chapter_urls = []
print("Manga ID: {}".format(manga_id))

content = requests.get(LINK).content
soup = BS(content, 'html.parser')

anchor_tags = soup.find_all("a")
for tag in anchor_tags:
    try:
        tag_link = tag["href"]
        if manga_id in tag_link:
            chapter_urls.append(tag_link)
    except KeyError:
        print("Couldnt find href for {}".format(tag))
chapter_urls = chapter_urls[1:]

with open("chapter_links.txt", "w") as f:
    f.write("\n".join(chapter_urls))
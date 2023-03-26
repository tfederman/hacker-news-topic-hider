import datetime
import sys
import time

import requests
from bs4 import BeautifulSoup

from algorithms import source_match, keyword_match
from settings import HEADERS, SOURCES, KEYWORDS, BASE_URL


while True:
    
    print(f"Starting fetch at {datetime.datetime.now()}")
    r = requests.get(BASE_URL, headers=HEADERS)

    if r.status_code != 200:
        sys.stderr.write(f"Bad status code: {r.status_code}\n")

    soup = BeautifulSoup(r.text, 'html.parser')

    for athing in soup.find_all(class_="athing"):

        try:
            titleline = athing.find(class_="titleline")
            subline = athing.next_sibling.find(class_="subline")
        except AttributeError:
            continue

        try:
            source = titleline.find(class_="sitestr").text.lower().strip()
        except AttributeError:
            source = ""

        title = titleline.find("a").text
        hide_path = subline.find(lambda e: e.attrs.get("href", "").startswith("hide?")).attrs["href"]

        hide = False

        if source_match(source):
            hide = True
            reason = "source"
        elif keyword_match(title):
            hide = True
            reason = "title"

        if hide:
            r = requests.get(f"{BASE_URL}{hide_path}", headers=HEADERS)
            print(f"hiding {reason}: {title} ({source})")
            time.sleep(1)

    time.sleep(5 * 60)

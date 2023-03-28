import re

from settings import SOURCES, SUBSTRINGS, KEYWORDS

def source_match(source):
    return any(source.lower().strip() == s.lower().strip() for s in SOURCES)

def title_match(title):
    return any(s.lower() in title.lower() for s in SUBSTRINGS) or \
            any(re.search(f"\\b{kw.lower()}\\b", title.lower()) for kw in KEYWORDS)

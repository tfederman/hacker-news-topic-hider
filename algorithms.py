from settings import SOURCES, KEYWORDS

def source_match(source):
    return any(source.lower().strip() == s.lower().strip() for s in SOURCES)

def keyword_match(title):
    return any(kw.lower() in title.lower() for kw in KEYWORDS)

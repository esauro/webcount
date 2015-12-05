from bs4 import BeautifulSoup
import urllib2
from collections import Counter


class BSTokenizer:

    def __init__(self, url):
        self.raw_content = urllib2.urlopen(url).read()
        self.soup = BeautifulSoup(self.raw_content, "html.parser")
        [s.extract() for s in self.soup(['style', 'script', '[document]', 'head', 'title', 'meta'])]

    def get_most_common_words(self, amount):
        text = self.soup.getText()
        frequencies = Counter(text.split())
        return frequencies.most_common(amount)


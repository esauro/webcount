# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
from collections import Counter


class BSTokenizer:
    """

    """

    def __init__(self, url):
        """
        Receive an url, reads it, create a beautiful object and extract sections don't wanted.

        Arguments:
            url (str): The string representation of an url to be analyzed
        """
        self.raw_content = urllib2.urlopen(url).read()
        self.soup = BeautifulSoup(self.raw_content, "html.parser")
        [s.extract() for s in self.soup(['style', 'script', '[document]', 'head', 'title', 'meta'])]

    def get_most_common_words(self, amount=100):
        """It gets all the text, split it, and count using a utility from collections standard libraries

        Arguments:
            amount (int): The amount of elements that should be returned

        Returns:
            List: A list with a list where first element is the word and second the number of
            repetitions [["hello", 10], ["bye", 4],...]
        """

        text = self.soup.getText()
        frequencies = Counter(text.split())
        return frequencies.most_common(amount)


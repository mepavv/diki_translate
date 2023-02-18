import requests
from bs4 import BeautifulSoup
import re
import contextlib


class Diki:
    def __init__(self, lang):
        """Klasa przyjmuje język, na który masz zamiar tłumaczyć.
        Dla przykładu:
        >>> diki = Diki("english")
        
        Wszystkie dozwolone języki to:
        "english", "german", "spanish", "italian", "french".
        """
        self.lang = lang


    def _bs4_info(self, word):
        langs = {
        "english": "angielskiego",
        "german": "niemieckiego",
        "spanish": 'hiszpanskiego',
        "italian": 'wloskiego',
        "french": 'francuskiego'
        }
        
        result = requests.get(f'https://www.diki.pl/slownik-{langs[self.lang]}?q={word}')
        soup = BeautifulSoup(result.text, 'html.parser')
        self.soup = soup


    def translation(self, word, exact_word = 1):
        """Zwraca znalezione tłumaczenia słowa (bez kontekstu).
        Dla przykładu:
        >>> diki = Diki("english")
        >>> list(diki.translation("use"))
        ['używać', 'korzystać (np. z telefonu, toalety)', 'zużywać', 'wykorzystywać (np. kogoś do swoich celów)', 'używać (w mowie lub w piśmie)',...]
        """
        
        r = self._bs4_info(word)
        div_class = self.soup.find_all('div','dictionaryEntity')

        for div in div_class:
            with contextlib.suppress(AttributeError):
                if exact_word == 1 and div.find("span", {"class": "hw"}).text.strip() == word or exact_word != 1:
                    for m in div.find_all('li', re.compile('^meaning\d+')):
                        for span in m.find_all('span', 'hw'):
                            yield span.text
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from services.TxtReader import TxtReader
from console.screen import sc

WORD_HEIGHT = 7

class WordView:
    def __init__(self):
        self.words = TxtReader().read_words()

    def display_word(self, word: str, pos: tuple) -> None:
        for i in range(WORD_HEIGHT):
            with sc.location(pos[0]+i, pos[1]):
                print(self.words[word][i], end="")
        return

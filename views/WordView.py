from services.TxtReader import TxtReader
from console.screen import sc

# Constants
WORD_HEIGHT = 7

# View of one word
class WordView:
    def __init__(self):
        # read words from TxtReader module
        self.words = TxtReader().read_words()

    # draw words at given position on the screen
    def display_word(self, word: str, pos: tuple) -> None:
        for i in range(WORD_HEIGHT):
            with sc.location(pos[0]+i, pos[1]):
                print(self.words[word][i], end="")
        return

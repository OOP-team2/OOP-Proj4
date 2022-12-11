# This is a Class for reading txt files
class TxtReader:
    # constructor for TxtReader Class
    def __init__(self) -> None:
        # member variable for hands
        self.hands = dict()
        # member variable for numbers
        self.numbers = dict()
        # member variable for numbers
        self.words = dict()

    # member function for reading hand from txt
    def read_hands(self) -> dict:
        for i in range(21):
            self.hands[str(i)] = []
            f = open(f"./src/img/hands/{i}.txt", encoding="UTF8")
            self.__read_file_to_dict(f, self.hands[str(i)])
            f.close()

        return self.hands

    # member function for reading numbers from txt
    def read_numbers(self) -> dict:
        for i in range(10):
            self.numbers[str(i)] = []
            f = open(f"./src/img/numbers/{i}.txt", encoding="UTF8")
            self.__read_file_to_dict(f, self.numbers[str(i)])
            f.close()

        return self.numbers

    # member function for reading words from txt
    def read_words(self) -> dict:
        self.words.update({
            "CALL": [],
            "HALF": [],
            "DIE": [],
            "EXIT": [],
            "PLAYER": [],
            "COM": [],
            "WON": [],
            "BETTING": [],
            "WIN": [],
            "LOSE": [],
            "R": []
        })

        for word in self.words.keys():
            f = open(f"./src/img/words/{word}.txt", encoding="UTF8")
            self.__read_file_to_dict(f, self.words[word])
            f.close()

        return self.words

    # member function reading file and save to container
    def __read_file_to_dict(self, f, container):
        k = 0
        while True:
            line = f.readline()
            if not line:
                break
            container.append(line)
            k += 1

# 테스트 파일을 읽어오는 클래스입니다.

class TxtReader:
    def __init__(self) -> None:
        self.hands = dict()
        self.numbers = dict()
        self.words = dict()

    def read_hands(self) -> dict:

        for i in range(21):
            self.hands[str(i)] = []
            f = open(f"../src/img/hands/{i}.txt", encoding="UTF8")
            self.__read_file_to_dict(f, self.hands[str(i)])
            f.close()

        return self.hands

    def read_numbers(self) -> dict:
        for i in range(10):
            self.numbers[str(i)] = []
            f = open(f"../src/img/numbers/{i}.txt", encoding="UTF8")
            self.__read_file_to_dict(f, self.numbers[str(i)])
            f.close()

        return self.numbers

    def read_words(self) -> dict:
        self.words.update({
            "CALL": [],
            "HALF": [],
            "DIE": [],
            "EXIT": [],
            "PLAYER": [],
            "COM": [],
            "WON": [],
            "BETTING": []
        })

        for word in self.words.keys():
            f = open(f"../src/img/words/{word}.txt", encoding="UTF8")
            self.__read_file_to_dict(f, self.words[word])
            f.close()

        return self.words

    def __read_file_to_dict(self, f, container):
        k = 0
        while True:
            line = f.readline()
            if not line:
                break
            container.append(line)
            k += 1

import string

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    def __init__(self):
        super().__init__("Eng", string.ascii_uppercase)
        self.__letters_num = len(string.ascii_uppercase)

    def is_en_letter(self, letter):
        if self.letters.count(letter) == 1:
            print("YES")
        else:
            print("NO")

    def letters_num(self):
        print(self.__letters_num)

    @staticmethod
    def example():
        print("ABCDE example text")

eng1 = EngAlphabet()

eng1.print()
eng1.letters_num()
eng1.is_en_letter("F")
eng1.is_en_letter("Щ")
eng1.example()


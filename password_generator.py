import random

SYMBOL = ('-', '.', ',', '!', '@', '#', '?', '$', '%', '^', '&', '*', '=', '+', '(', ')',
          '[', ']', '{', '}', '<', '>', ';', ':')
CHAR = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
UPPER_CHAR = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
              'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')


class Password:
    def __init__(self, min_length_=12, max_length_=18, min_unique_letters_=6, diff_register_=True,
                 min_unique_digits_=4, min_digits_=4, min_unique_symbol_=4, symbol_in_pass_=4) -> None:
        self.min_length = min_length_
        self.max_length = max_length_
        self.diff_register = diff_register_
        self.min_unique_letters = min_unique_letters_
        self.min_unique_digits = min_unique_digits_
        self.min_digits = min_digits_
        self.min_unique_symbol = min_unique_symbol_
        self.symbol_in_pass = symbol_in_pass_
        self.password = ""
        self.__check_parameters()

    def get_password(self) -> str:
        self.__generate_password()
        self.password = ""
        """shuffling the list and creating a string"""
        while len(self.__password) != 0:
            index = len(self.__password) - 1
            self.password += self.__password.pop(random.randint(0, index))
        return self.password

    def __generate_password(self) -> list[str]:
        """long list with all letters/symbols"""
        self.__password = []
        self.__password += self.__generate_chars()
        self.__password += self.__generate_digits()
        self.__password += self.__generate_symbols()

        """random size of password"""
        min_size = self.min_unique_letters + self.min_digits + self.symbol_in_pass
        self.size_of_password = random.randint(min_size, self.max_length)

        """addition not unique letters/symbols"""
        all_symbols = [SYMBOL, CHAR, UPPER_CHAR]
        while len(self.__password) != self.size_of_password:
            if self.diff_register is True:
                self.__password.append(random.choice(all_symbols[random.randint(0, 2)]))
            else:
                self.__password.append(random.choice(all_symbols[random.randint(0, 1)]))
        return self.__password

    def __generate_chars(self) -> list[str]:
        """generation a list with unique chars"""
        all_symbols = [SYMBOL, CHAR, UPPER_CHAR]
        letters_uniq = set()
        while len(letters_uniq) != self.min_unique_letters:
            if self.diff_register:
                letters_uniq.add(random.choice(all_symbols[random.randint(1, 2)]))
            elif self.diff_register is False:
                if len(letters_uniq) < self.min_unique_letters:
                    letters_uniq.add(random.choice(CHAR))
        letters = list(letters_uniq)
        return letters

    def __generate_digits(self) -> list[str]:
        """generation a list with unique digits"""
        digit_uniq = set()
        digits = []
        while True:
            if len(digit_uniq) < self.min_unique_digits:
                digit_uniq.add(str(random.randint(0, 9)))
            elif len(digit_uniq) == self.min_digits and isinstance(digit_uniq, list) is False:
                digit_uniq = list(digit_uniq)
                digits = digit_uniq
            elif self.min_digits != len(digits):
                digits.append(str(random.randint(0, 9)))
            else:
                break
        return digits

    def __generate_symbols(self) -> list[str]:
        """generation a list with unique symbols"""
        symbol_uniq = set()
        symbols = []
        while True:
            if len(symbol_uniq) < self.min_unique_symbol:
                symbol_uniq.add(random.choice(SYMBOL))
            elif len(symbol_uniq) == self.min_unique_symbol and isinstance(symbol_uniq, list) is False:
                symbol_uniq = list(symbol_uniq)
                symbols = symbol_uniq
            elif self.symbol_in_pass != len(symbols):
                symbols.append(random.choice(SYMBOL))
            else:
                break
        return symbols

    def __check_parameters(self) -> None:
        """checking input parameters"""
        try:
            if isinstance(self.min_length, int) is not True:
                exit("Wrong parameters! min_length must be only integer type!")
            if isinstance(self.max_length, int) is not True:
                exit("Wrong parameters! max_length must be only integer type!")
            if isinstance(self.min_unique_letters, int) is not True:
                exit("Wrong parameters! min_unique_letters must be only integer type!")
            if isinstance(self.min_unique_digits, int) is not True:
                exit("Wrong parameters! min_unique_digits must be only integer type!")
            if isinstance(self.min_digits, int) is not True:
                exit("Wrong parameters! min_digits must be only integer type!")
            if isinstance(self.min_unique_symbol, int) is not True:
                exit("Wrong parameters! min_unique_symbol must be only integer type!")
            if isinstance(self.symbol_in_pass, int) is not True:
                exit("Wrong parameters! symbol_in_pass must be only integer type!")
            if isinstance(self.diff_register, bool) is not True:
                exit("Wrong parameters! diff_register must be only boolean type!")
            if self.min_length > self.max_length:
                exit("Wrong parameters! max_length must be more than min_length!")
            if self.min_digits < self.min_unique_digits:
                exit("Wrong parameters! min_digits must be more than min_unique_digits!")
            if self.symbol_in_pass < self.min_unique_symbol:
                exit("Wrong parameters! symbol_in_pass must be more than min_unique_symbol!")
            if self.min_length < (self.min_unique_letters + self.min_digits + self.symbol_in_pass) > self.max_length:
                exit(f"Wrong parameters!\n"
                     f"min:{self.min_length} < "
                     f"all_uniq:{self.min_unique_letters + self.min_digits + self.symbol_in_pass} < "
                     f"max:{self.max_length}")
            print("Input parameters are valid!")
        except Exception:
            exit("Exception: Type error!")


if __name__ == '__main__':
    min_length = 12
    max_length = 18
    min_unique_letters = 6  #
    diff_register = True
    min_unique_digits = 4
    min_digits = 5  #
    min_unique_symbol = 4  #
    symbol_in_pass = 5

    password = Password(min_length, max_length, min_unique_letters,
                        diff_register, min_unique_digits, min_digits,
                        min_unique_symbol, symbol_in_pass)

    for i in range(10):
        print(password.get_password())



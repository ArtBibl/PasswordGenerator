import pytest
from password_generator import Password

char = set("abcdefghijklmnopqrstuvwxyz")
upper_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
symbol = set("-.,!@#?$%^&*=+()[]{}<>;:")
digits = set("0123456789")


def test_for_size_password():
    min_length = 12
    max_length = 18
    password = Password(min_length_=min_length, max_length_=max_length)
    result = password.get_password()
    assert len(result) >= min_length and len(result) <= max_length


def test_for_dif_register_char():
    diff_register = True
    password = Password(diff_register_=diff_register)
    result = password.get_password()
    result = True if set(result) & upper_char else False
    assert result is diff_register


def test_for_count_min_unique_char():
    min_unique_letters = 6
    password = Password(min_unique_letters_=min_unique_letters)
    result = password.get_password()
    result1 = set(result) & char
    result2 = set(result) & upper_char
    result = result1 | result2
    assert min_unique_letters <= len(result)


def test_for_min_unique_digits():
    min_unique_digits = 4
    password = Password(min_unique_digits_=min_unique_digits)
    result = password.get_password()
    result = set(result) & digits
    assert min_unique_digits <= len(result)


def test_for_min_digits():
    min_digits = 4
    password = Password(min_digits_=min_digits)
    result = password.get_password()
    result = set(result) & digits
    assert min_digits <= len(result)


def test_for_min_unique_symbol():
    min_unique_symbol = 4
    password = Password(min_unique_symbol_=min_unique_symbol)
    result = password.get_password()
    result = set(result) & symbol
    assert min_unique_symbol <= len(result)


def test_for_count_symbol_in_pass():
    symbol_in_pass = 5
    password = Password(symbol_in_pass_=symbol_in_pass)
    result = password.get_password()
    dig = 0
    for i in result:
        if i in symbol:
            dig += 1
    assert symbol_in_pass <= dig

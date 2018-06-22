#Python Turkish

from string import punctuation

lower_case = "abcçdefgğhıijklmnoöpqrsştuüvwxyz"
upper_case = "ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ"

def capitalize(string):

    capital=lower_case.index(string[0])
    string= string.strip(string[0])
    capitalized = upper_case[capital] + string
    return capitalized


def upper_caser(string):
    for char in string:
        if char in lower_case:
            capital = lower_case.index(char)
            captalized_char = upper_case[capital]
            print(captalized_char,end="")

        elif char in punctuation:
            print(char,end="")

        else:
            print(char,end="")





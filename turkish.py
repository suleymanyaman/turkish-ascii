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
    holder = ""
    for char in string:
        index = lower_case.index(char)
        holder = holder + upper_case[index]

    return holder



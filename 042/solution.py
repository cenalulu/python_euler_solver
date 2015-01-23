#! encoding: utf8
from profile_decorate import profile
from itertools import count

"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""


def gen_triangle():
    for n in count(1):
        yield n * (n + 1) / 2


@profile
def main():
    word_line = list()
    with open('./p042_words.txt') as word_file:
        word_line = word_file.readline()
    word_list = [word.strip('"') for word in word_line.split(',')]
    max_word_len = 0
    for word in word_list:
        max_word_len = max(max_word_len, len(word))
    max_possbile_triangle_number = 26 * max_word_len
    triangle_list = list()
    for number in gen_triangle():
        if number > max_possbile_triangle_number:
            break
        else:
            triangle_list.append(number)
    total_triangle_num = 0
    for word in word_list:
        word_num = sum([ord(char) - ord('A') + 1 for char in list(word)])
        if word_num in triangle_list:
            total_triangle_num += 1
    print('total triangle count is {}'.format(total_triangle_num))


if __name__ == '__main__':
    main()

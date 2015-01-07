"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""

unit_dict = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
             'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens_dict = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'}


def translate_to_word(i):
    word_form = ''
    hundred_num = int(i / 100)
    tens_num = int((i - hundred_num * 100) / 10)
    unit_num = i - hundred_num * 100 - tens_num * 10
    if i == 1000:
        return 'onethousand'
    if hundred_num > 0:
        word_form += unit_dict[int(i / 100)]
        word_form += 'hundred'
        if tens_num == 0 and unit_num == 0:
            # it's special hundreds num
            return word_form
        word_form += 'and'
    if tens_num > 1:
        word_form += tens_dict[tens_num]
        if unit_num > 0:
            word_form += unit_dict[unit_num]
        return word_form
    else:
        word_form += unit_dict[i - hundred_num * 100]
        return word_form


def main(*args, **kwargs):
    total_lenth = 0
    for i in range(1, 1001):
        word_of_num = translate_to_word(i)
        total_lenth += len(word_of_num)
        print word_of_num
    print total_lenth


if __name__ == '__main__':
    main()

#! encoding: utf8
from profile_decorate import profile
from itertools import permutations
from binascii import b2a_uu

"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code
for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value,
 taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text,
  restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random
 bytes. The user would keep the encrypted message and the encryption key in different locations, and without
  both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
 If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
 The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt
(right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the
plain text must contain common English words, decrypt the message and find the sum of the ASCII values in
the original text.
"""


@profile
def main():
    INPUT_FILE = './p059_cipher.txt'
    ascii_array = [i for i in range(97, 123)]
    normal_char_array = [i for i in range(97, 123)]
    capital_char_array = [i for i in range(65, 91)]

    dict_file = '/usr/share/dict/words'
    dict_array = dict()
    with open(dict_file) as dict_fh:
        for word in dict_fh.readlines():
            word = word.rstrip('\n')
            dict_array[word] = True

    current_max_hit = 0
    with open(INPUT_FILE) as fh:
        for line in fh.readlines():
            chars = line.split(',')
            current_answer = list()
            for encrypt_char1 in range(97, 123):
                for encrypt_char2 in range(97, 123):
                    for encrypt_char3 in range(97, 123):
                        encrypt_str = (encrypt_char1, encrypt_char2, encrypt_char3)
                        for idx, single_ascii in enumerate(chars):
                            decrypt_char = encrypt_str[idx%3] ^ int(single_ascii)
                            if not 0 <= decrypt_char <= 126:
                                break
                        else:
                            word_cnt = 0
                            word_now = list()
                            for idx, single_ascii in enumerate(chars):
                                decrypt_char = encrypt_str[idx%3] ^ int(single_ascii)
                                if decrypt_char not in normal_char_array and decrypt_char not in capital_char_array:
                                    try:
                                        if len(word_now) >= 3:
                                            if dict_array[''.join(word_now)]:
                                                word_cnt += 1
                                    except KeyError:
                                        pass
                                    word_now = list()
                                else:
                                    word_now.append(chr(decrypt_char))
                            if current_max_hit < word_cnt:
                                current_max_hit = word_cnt
                                current_answer = encrypt_str

            result_array = list()
            sum_up = 0
            for idx, single_ascii in enumerate(chars):
                decrypt_char = current_answer[idx%3] ^ int(single_ascii)
                sum_up += decrypt_char
                result_array.append(chr(decrypt_char))
            print ''.join(result_array)
            print sum_up


if __name__ == '__main__':
    main()

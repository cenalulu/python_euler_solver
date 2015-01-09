def name_char_score(name=None):
    name_score = 0
    for char in str(name):
        name_score += ord(char) - ord('A') + 1
    return name_score


def main():
    name_dict = {}
    fh = open('./names.txt')
    single_line = fh.readline()
    for name in single_line.split(','):
        name = name.strip('"')
        name_dict[name] = name_char_score(name)

    rank = 1
    total_score = 0
    for name in sorted(name_dict):
        total_score += rank * name_dict[name]
        if name == 'COLIN':
            print rank, name_dict[name]
        rank += 1

    print total_score


if __name__ == '__main__':
    main()

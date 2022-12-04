from pathlib import Path
import string


def part1(lines):
    t = 0
    for line in lines:
        lenght = int(len(line) / 2)
        a = line[:lenght]
        b = line[lenght:]
        # trouver les lettres en commun grace au set intersection :
        common = set(a).intersection(b)
        # convert set to str and use string.ascii_letters.index to find the value of each letter.
        t += string.ascii_letters.index(''.join(common)) + 1

    return t


def part2(lines):
    current = []
    t = 0
    for line in lines:
        current.append(line)
        if len(current) >= 3:
            common = list(set(current[0]) & set(current[1]) & set(current[2]))[0]
            t += string.ascii_letters.index(common) + 1
            current = []
    
    return t


if __name__ == '__main__':
    lines = Path('input.txt').read_text().rstrip().split('\n')

    p1 = part1(lines)
    print(p1)

    p2 = part2(lines)
    print(p2)
from pathlib import Path


def part1(lines):
    for i, _ in enumerate(lines):
        if len(set(lines[i:i+4])) == 4:
            return len(lines[:i+4])
            




def part2(lines):
    for i, _ in enumerate(lines):
        if len(set(lines[i:i+14])) == 14:
            return len(lines[:i+14])


if __name__ == '__main__':
    lines = Path('input.txt').read_text().rstrip()
    # print(lines)
    p1 = part1(lines)
    print(p1)

    p2 = part2(lines)
    print(p2)
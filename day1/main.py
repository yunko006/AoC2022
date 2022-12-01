from pathlib import Path


def part1(lines:list) -> int and list:
    l = []
    t = 0
    for line in lines:
        if not line:
            l.append(t)
            t = 0

        else:
            t += int(line)
    
    return max(l), l


def part2(list_for_part2:list) -> int:
    reversed_list = sorted(list_for_part2)[::-1]
    top3 = reversed_list[:3]

    total = 0
    for i in top3:
        total += int(i)

    return total


if __name__ == '__main__':
    lines = Path('input.txt').read_text().rstrip().split('\n')

    part1_answer, list_for_part2  = part1(lines)
    print(part1_answer)

    p2 = part2(list_for_part2)
    print(p2)
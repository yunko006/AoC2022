from pathlib import Path


def part1(lines):
    count = 0
    for line in lines[:]:
        # parse number before the comma
        f = line.index('-')
        v = line.index(',')
        num1, num2 = int(line[:f]), int(line[f+1:v])
        # parse after the comma
        subline = line[v+1:]
        x = subline.index('-')
        num3, num4 = int(subline[:x]), int(subline[x+1:])


        x = [x for x in range(num1, num2 + 1)]
        y = [y for y in range(num3, num4 + 1)]
        # check if one range is in another one
        if all(item in y for item in x) or all(item in x for item in y):
            count += 1

    return count

def part2(lines):
    count = 0
    for line in lines[:]:
        # parse number before the comma
        f = line.index('-')
        v = line.index(',')
        num1, num2 = int(line[:f]), int(line[f+1:v])
        # parse after the comma
        subline = line[v+1:]
        x = subline.index('-')
        num3, num4 = int(subline[:x]), int(subline[x+1:])

        x = [x for x in range(num1, num2 + 1)]
        y = [y for y in range(num3, num4 + 1)]
        
        if num1 in y or num2 in y:
            count += 1
        
        elif num3 in x or num4 in x:
            count += 1

    return count


if __name__ == '__main__':
    lines = Path('input.txt').read_text().rstrip().split('\n')

    p1 = part1(lines)
    print(p1)

    p2 = part2(lines)
    print(p2)

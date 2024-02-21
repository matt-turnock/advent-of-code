import re


def part1():
    count = 0

    with open('strings', 'r') as f:
        for line in f:
            if re.search(r'(.*[aeiou]){3}', line):
                if re.search(r'(.)\1', line):
                    if not re.search(r'ab|cd|pq|xy', line):
                        count += 1

    return count


def part2():
    count = 0

    with open('strings', 'r') as f:
        for line in f:
            if re.search(r'(..).*\1', line):
                if re.search(r'(.).\1', line):
                    count += 1

    return count


print(part1())
print(part2())

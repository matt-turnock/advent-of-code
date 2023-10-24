def bad_string(line):
    if 'ab' in line or 'cd' in line or 'pq' in line or 'xy' in line:
        return False
    else:
        return True


def doubleletter(line):
    for index in range(len(line) - 1):
        if line[index] == line[index + 1]:
            return True

    return False


def vowel_check(line):
    vowels = ['a', 'e', 'i', 'o', 'u']
    total_vowels = []

    for letter in line:
        if letter in vowels:
            total_vowels.append(letter)

    if len(total_vowels) > 2:
        return True
    else:
        return False


def pair(line):
    for index in range(len(line) - 1):
        if f"{line[index]}{line[index + 1]}" in line[index + 2:]:
            return True
        else:
            return False


def sandwich(line):
    for index in range(len(line) - 1):
        


nice_stringsv1 = []
nice_stringsv2 = []

try:
    with open('./strings', 'r') as f:
        for line in f:
            if bad_string(line) and doubleletter(line) and vowel_check(line):
                nice_stringsv1.append(line)
            if pair(line) and sandwich(line):
                nice_stringsv2.append(line)
except FileNotFoundError as error:
    print(error)


print(f"Part1: {len(nice_stringsv1)}")
print(f"Part2: {len(nice_stringsv2)}")

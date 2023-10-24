import hashlib

puzzle_input = "iwrupvqb"

hash = ""
counter = 1

while True:
    hash = hashlib.md5(f"{puzzle_input}{counter}".encode())
    first_five = hash.hexdigest()

    if first_five[:6] == "000000":
        print(counter)
        break
    counter += 1

def file_read():
    try:
        with open('./directions', 'r') as f:
            for line in f:
                return line
    except FileNotFoundError as error:
        print(error)


sx = 0
sy = 0
rx = 0
ry = 0
visited_houses = [(sx, sy), (rx, ry)]

line = file_read()

for index, direction in enumerate(line):
    if index % 2:
        if direction == '>':
            sy += 1
        elif direction == 'v':
            sx -= 1
        elif direction == '<':
            sy -= 1
        elif direction == '^':
            sx += 1

        visited_houses.append((sx, sy))
    else:
        if direction == '>':
            ry += 1
        elif direction == 'v':
            rx -= 1
        elif direction == '<':
            ry -= 1
        elif direction == '^':
            rx += 1

        visited_houses.append((rx, ry))

print(len(set(visited_houses)))

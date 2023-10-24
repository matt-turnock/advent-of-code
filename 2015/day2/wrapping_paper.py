def paper():
    try:
        with open('./dimensions', 'r') as f:
            total = 0
            for index, line in enumerate(f):
                sides = line.split('x')

                length = int(sides[0])
                width = int(sides[1])
                height = int(sides[2].strip())

                pick_middle = [length, width, height]
                pick_middle.sort()

                subtotal = (2 * length * width) + (2 * width * height) + (2 * height * length) + (int(min(length, width, height)) * pick_middle[1])
                total += subtotal

            print(total)
    except FileNotFoundError as error:
        print(error)


def ribbon():
    try:
        with open('./dimensions', 'r') as f:
            total = 0
            for index, line in enumerate(f):
                sides = line.split('x')

                length = int(sides[0])
                width = int(sides[1])
                height = int(sides[2].strip())

                pick_middle = [length, width, height]
                pick_middle.sort()

                subtotal = pick_middle[0] + pick_middle[0] + pick_middle[1] + pick_middle[1]
                subtotal += pick_middle[0] * pick_middle[1] * pick_middle[2]
                total += subtotal

            print(total)
    except FileNotFoundError as error:
        print(error)


paper()
ribbon()

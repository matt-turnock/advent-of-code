try:
    with open('./steps', 'r') as f:
        step = f.readlines()
        steps = step[0]

        floor = 0

        for index, item in enumerate(steps):
            if item == "(":
                floor += 1
            elif item == ")":
                floor -= 1

            if floor < 0:
                print(index)
                exit()
except FileNotFoundError as error:
    print(error)

# pseudo:
# read in steps file
# count (
# count )
# calculate the difference starting at 0

try:
    with open('./steps', 'r') as f:
        step = f.readlines()
        steps = step[0]
        left = steps.count('(')
        right = steps.count(')')
        floor = 0 + (left - right)
        print(floor)
except FileNotFoundError as error:
    print(error)

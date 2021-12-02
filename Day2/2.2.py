with open("input1.txt") as f:
    lines = f.readlines()
    f.close()
total_horizontal = 0
total_vertical = 0
aim = 0

line_dict = {}
for line in lines:
    word = line[:-3]
    num = int(line[-2])

    if word == "forward":
        total_horizontal += num
        total_vertical += aim * num
    elif word == "up":
        aim -= num
    elif word == "down":
        aim += num

print(total_horizontal * total_vertical)
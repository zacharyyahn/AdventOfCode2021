with open("input1.txt") as f:
    lines = f.readlines()
    f.close()
total_horizontal = 0
total_vertical = 0

line_dict = {}
for line in lines:
    word = line[:-3]
    num = int(line[-2])

    if word == "forward":
        total_horizontal += num
    elif word == "up":
        total_vertical -= num
    elif word == "down":
        total_vertical += num

print(total_horizontal * total_vertical)



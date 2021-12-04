with open("input1.txt") as f:
    lines = f.readlines()
    f.close

length = len(lines) - 1
lines = [line.strip("\n") for line in lines]

def get_oxygen(current_index, array):
    if current_index == length or len(array) == 1:
        return array[0]
    one_array = []
    zero_array = []
    for line in array:
        if line[current_index] == "0":
            zero_array.append(line)
        elif line[current_index] == "1":
            one_array.append(line)
    if len(one_array) >= len(zero_array):
        return get_oxygen(current_index + 1, one_array)
    else:
        return get_oxygen(current_index + 1, zero_array)

def get_co2(current_index,array):
    if current_index == length or len(array) == 1:
        return array[0]
    one_array = []
    zero_array = []
    for line in array:
        if line[current_index] == "0":
            zero_array.append(line)
        elif line[current_index] == "1":
            one_array.append(line)
    if len(zero_array) > len(one_array):
        return get_co2(current_index + 1, one_array)
    else:
        return get_co2(current_index + 1, zero_array)

ox = get_oxygen(0, lines)
co2 = get_co2(0, lines)
ox = int("".join(ox), 2)
co2 = int("".join(co2), 2)
print(ox)
print(co2)
print(ox * co2)



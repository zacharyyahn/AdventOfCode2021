with open("input1.txt") as f:
    lines = f.readlines()
    f.close

length = len(lines) -1 
sum_arr = [0 for i in range(len(lines[0])-1)]
for line in lines:
    for i in range(len(line)-1):
        sum_arr[i] += int(line[i])

half = float(length) / 2

gamma_array = []
epsilon_array = []
for num in sum_arr:
    if num < half:
        gamma_array.append("0")
        epsilon_array.append("1")
    if num > half:
        gamma_array.append("1")
        epsilon_array.append("0")

print(gamma_array)
print(epsilon_array)
gamma = int("".join(gamma_array),2)
print(gamma)
epsilon = int("".join(epsilon_array),2)
print(epsilon)
print(gamma * epsilon)



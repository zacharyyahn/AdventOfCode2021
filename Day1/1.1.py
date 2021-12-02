with open("input1.txt") as f:
    lines = f.readlines()
    f.close()
print(lines)
lines = [int(line.strip("\n")) for line in lines]
num_greater = 0
for i in range(1,len(lines)):
    if lines[i] > lines[i-1]:
        num_greater += 1

print(num_greater)

    
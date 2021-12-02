with open("input1.txt") as f:
    lines = f.readlines()
    f.close()

lines = [int(line.strip("\n")) for line in lines]
chunks = []
for i in range(2, len(lines)):
    chunks.append(lines[i] + lines[i-1] + lines[i-2])
num_greater = 0
for i in range(1, len(chunks)):
    if chunks[i] > chunks[i-1]:
        num_greater += 1
print(num_greater)
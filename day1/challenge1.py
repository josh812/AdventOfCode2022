with open('input.txt', 'r') as file:
	inputData = []
	for line in file.read().strip().split("\n"):
		inputData.append(line)

max = 0
count = 0
for line in inputData:
	if line != '':
		count += int(line)
	else:
		if count > max:
			max = count
		count = 0

print(max)
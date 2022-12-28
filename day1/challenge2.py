with open('input.txt', 'r') as file:
	inputData = []
	for line in file.read().strip().split("\n"):
		inputData.append(line)

first = 0
second = 0
third = 0
count = 0

for line in inputData:
	if line != '':
		count += int(line)
	else:
		if count > first:
			third = second
			second = first
			first = count
		if count > second and count < first:
			third = second
			second = count
		if count > third and count < second and count < first:
			third = count
		count = 0

print(first + second + third)
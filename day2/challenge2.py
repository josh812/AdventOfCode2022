with open('input.txt', 'r') as file:
	array = []
	for line in file.read().strip().split('\n'):
		array.append(line)

inputData = []

for line in array:
	inputData.append(line.split(' '))

score = 0

for round in inputData:
	if round[0] == 'A' and round[1] == 'X':
		score += 3
	elif round[0] == 'A' and round[1] == 'Y':
		score += 4
	elif round[0] == 'A' and round[1] == 'Z':
		score += 8
	elif round[0] == 'B' and round[1] == 'X':
		score += 1
	elif round[0] == 'B' and round[1] == 'Y':
		score += 5
	elif round[0] == 'B' and round[1] == 'Z':
		score += 9
	elif round[0] == 'C' and round[1] == 'X':
		score += 2
	elif round[0] == 'C' and round[1] == 'Y':
		score += 6
	elif round[0] == 'C' and round[1] == 'Z':
		score += 7

print(score)
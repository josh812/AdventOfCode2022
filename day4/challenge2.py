with open('input.txt', 'r') as file:
	#format = [[#, #], [#, #]]
	inputData = []
	for line in file.read().strip().split('\n'):
		pair = []
		pair.append(line.split(',')[0].strip().split('-'))
		pair.append(line.split(',')[1].strip().split('-'))
		inputData.append(pair)

count = 0

for elf_pair in inputData:
	elf1 = [int(elf_pair[0][0]), int(elf_pair[0][1])]
	elf2 = [int(elf_pair[1][0]), int(elf_pair[1][1])]

	if elf1[0] in range(elf2[0], elf2[1]+1) or elf1[1] in range(elf2[0], elf2[1]):
		count += 1
	elif elf2[0] in range(elf1[0], elf1[1]+1) or elf2[1] in range(elf1[0], elf1[1]):
		count += 1

print(count)
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
	elfRange1 = int(elf_pair[0][1])-int(elf_pair[0][0])
	elfRange2 = int(elf_pair[1][1])-int(elf_pair[1][0])
	elf1 = elf_pair[0]
	elf2 = elf_pair[1]

	if elfRange1 > elfRange2:
		if int(elf2[0]) >= int(elf1[0]) and int(elf2[1]) <= int(elf1[1]):
				count += 1
	elif elfRange2 > elfRange1:
		if int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]):
				count += 1
	elif elfRange1 == elfRange2:
		if elf1[0] == elf2[0] and elf1[1] == elf2[1]:
			count += 1

print(count)
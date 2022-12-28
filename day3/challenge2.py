with open('input.txt', 'r') as file:
	inputData = []
	for line in file.read().strip().split('\n'):
		inputData.append(line)

lowerAlphabet = 'abcdefghijklmnopqrstuvwxyz'
upperAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def findPriority(letter):
	priority = 0
	if letter.isupper():
		priority = (upperAlphabet.rfind(letter)+27)
	elif letter.isupper() == False:
		priority = (lowerAlphabet.rfind(letter)+1)
	return priority

def findCommonItem(rucksack1, rucksack2, rucksack3):
	commonItem = str
	for item1 in rucksack1:
		for item2 in rucksack2:
			for item3 in rucksack3:
				if item1 == item2 and item2 == item3 and item1 == item3:
					commonItem = str(item1)
					return str(commonItem)
	return('a')

sumOfPriorities = 0

elf1 = []
elf2 = []
elf3 = []

for rucksack in inputData:
	if len(elf1) == 0:
		for itemLocation in range(len(rucksack)):
			elf1.append(rucksack[itemLocation])
	elif len(elf2) == 0:
		for itemLocation in range(len(rucksack)):
			elf2.append(rucksack[itemLocation])
	elif len(elf3) == 0:
		for itemLocation in range(len(rucksack)):
			elf3.append(rucksack[itemLocation])
	else:
		sumOfPriorities += findPriority(findCommonItem(elf1, elf2, elf3))
		elf1 = rucksack
		elf2 = []
		elf3 = []

#Accounts for last set of rucksacks
sumOfPriorities += findPriority(findCommonItem(elf1, elf2, elf3))

print(sumOfPriorities)
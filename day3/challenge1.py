with open('input.txt', 'r') as file:
	inputData = []
	for line in file.read().strip().split('\n'):
		inputData.append(line)

lowerAlphabet = 'abcdefghijklmnopqrstuvwxyz'
upperAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sumOfPriorities = 0

for rucksack in inputData:
	sharedItem = str
	compartment1 = []
	compartment2 = []
	rucksackCmprtmntLen = int(len(rucksack)/2)

	for itemLocation in range(rucksackCmprtmntLen):
		compartment1.append(rucksack[itemLocation])
	for itemLocation in range(rucksackCmprtmntLen):
		compartment2.append(rucksack[itemLocation + rucksackCmprtmntLen])

	for item1 in compartment1:
		for item2 in compartment2:
			if item1 == item2:
				sharedItem = item1

	if sharedItem.isupper():
		sumOfPriorities += upperAlphabet.rfind(sharedItem)+27
	elif sharedItem.isupper() == False:
		sumOfPriorities += lowerAlphabet.rfind(sharedItem)+1

print(sumOfPriorities)
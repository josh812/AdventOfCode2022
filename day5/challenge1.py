with open('input.txt', 'r') as file:
	stack_strings, moves = (i.splitlines() for i in file.read().strip("\n").split("\n\n"))

stacks = {int(digit):[] for digit in stack_strings[-1].replace(' ', '')}
indexes = [index for index, char in enumerate(stack_strings[-1]) if char != ' ']

def loadStacks():
	for string in stack_strings[:-1]:
		stack_num = 1
		for index in indexes:
			if string[index] != ' ':
				stacks[stack_num].append(string[index])
			stack_num += 1

loadStacks()

for move in moves:
	num_to_move = int(move.split('move ')[1].split(' from')[0])
	where_to_take = int(move.split('from ')[1].split(' to')[0])
	where_to_move = int(move.split('to ')[1])

	for movement in range(num_to_move):
		crate = stacks[where_to_take][0]
		del stacks[where_to_take][0]

# print("\nStacks:")
# for stack in stacks:
# 	print(stack, stacks[stack])

# print(moves)
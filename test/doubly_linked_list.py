import numpy as np

import numpy as np


class Node:
	""" Node class

			up
			 |
	left - data - right
			 |
		   down
	"""
	
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None
		self.up = None
		self.down = None
	
	def __iter__(self):
		return self


def display(dll_ptr):
	""" Prints the 2D dll according to their positions similar to
		printing a 2D array.

	input:
		dll_ptr: the head (most upper left node) of a 2D dll.

	output:
		None
	"""
	right_ptr = None
	down_ptr = dll_ptr
	
	while down_ptr != None:
		right_ptr = down_ptr
		
		while right_ptr != None:
			print(right_ptr.data, end=' ')
			right_ptr = right_ptr.right
		print()
		down_ptr = down_ptr.down


def constructDoublyLinkedListLoop(arr) -> Node:
	""" Converts a 2D array into a 2D doubly linked list with loops.

	input:
		arr: 2D array to turn into a 2D DLL

	output:
		top_left_ptr: head (top left node) of the 2D DLL of the input arr.
	"""
	
	top_left_ptr = Node(arr[0][0])
	
	# print(top_left_ptr, type(top_left_ptr), sep='\n')
	
	"""top_left_ptr= arr[0][0] """
	"""top_left_ptr.data = arr[0][0]"""
	x = 0
	y = 0
	downside_ptr = top_left_ptr
	'''
	[[4 2 4 1 2]
    [6 1 7 1 8]
    [9 8 6 7 9]
    [4 2 8 8 4]
    [9 4 4 0 2]]
    
    5 x 5 matrix
    
	'''
	
	for y in range(0, arr.shape[0]):       # 0 ~ hight - 1
		for x in range(0, arr.shape[1]):   # 0 ~ width - 1
			right_ptr = Node(arr[x][y])
			
			if y == 0:
				right_ptr.down = arr[x][y + 1]
				if x == 0:
					right_ptr.right = arr[x + 1][y]
				elif x == (arr.shape[1] - 1):
					right_ptr.left = arr[x - 1][y]
				else:
					right_ptr.right = arr[x + 1][y]
					right_ptr.left = arr[x - 1][y]
			elif y == (arr.shape[0] - 1):
				right_ptr.up = arr[x][y - 1]
				if x == 0:
					right_ptr.right = arr[x + 1][y]
				elif x == (arr.shape[1] - 1):
					right_ptr.left = arr[x - 1][y]
				else:   # 0 ~ n
					right_ptr.right = arr[x + 1][y]
					right_ptr.left = arr[x - 1][y]
			elif x == 0:
				right_ptr.up = arr[x][y - 1]
				right_ptr.down = arr[x][y + 1]
				right_ptr.right = arr[x + 1][y]
			elif x == (arr.shape[1] - 1):
				right_ptr.up = arr[x][y - 1]
				right_ptr.down = arr[x][y + 1]
				right_ptr.left = arr[x - 1][y]
			else:
				right_ptr.up = arr[x][y - 1]
				right_ptr.down = arr[x][y + 1]
				right_ptr.left = arr[x - 1][y]
				right_ptr.right = arr[x + 1][y]
			
			top_left_ptr.data
			
	
	return right_ptr
	# return top_left_ptr


N = 5  # you can try other N if you want
arr = np.random.randint(0, 10, size=(N, N))

temp = constructDoublyLinkedListLoop(arr)

display(temp)

print(dict.__doc__)


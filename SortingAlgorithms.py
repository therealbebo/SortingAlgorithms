# Various Sorting Algorithms #
from random import *

def bogoSort(l):
		## First checks if all values are sorted ##
	while not all(l[i] <= l[i + 1] for i in range(len(l) - 1)):
		## If not, then list is randomized ##
		shuffle(l)
	return l

def bubbleSort(l):
	for j in range(len(l)):
		## j represents the number bubble sorts already performed ##

		for i in range(len(l-1)):
		## i represents the index at which bubble sort is taking place ##
		## i ranges between 0 & (list length - 1 - j) 
		## As end of the list has already been sorted (eliminating redundancy) ##

			if l[i] > l[i+1]:
				l[i], l[i+1] = l[i+1], l[i]
		## Operation above swaps elements in list if leftmost value is greater
	return l	

def mergeSort(l):
	if len(l) > 1:
		## Halve list until many 1 element lists are created ##
		left, right = l[:len(l)//2], l[len(l)//2:]
		left, right = mergeSort(left), mergeSort(right)

		## Clear original list ##
		l = []

		# Merges the list until 1 remains #
		while len(left) > 0 and len(right) > 0:
			if left[0] < right[0]:
				l.append(left[0]), left.pop(0)
			else:
				l.append(right[0]), right.pop(0)
		[l.append(i) for i in left]
		[l.append(i) for i in right]
	return l


if __name__ == "__main__":
	nElements = 20
	unsortedList = [randint(0,nElements) for x in range (nElements)]
	unsortedList = [x for x in range(nElements)]
	shuffle(unsortedList)
	print(unsortedList)
	


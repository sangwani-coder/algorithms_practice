#!/usr/bin/env python3

# insertion_sort.py
""" file contains a simple implementation 
	of the insertion sort algorithm.
"""


def insertion_sort(arr=[]):
	"""Sorts an unsorted list in nondescending order
		using the INSERTION SORT algorithm
		param: Unsorted list of numbers
		return: Sorted list of numbers non-descending
	"""
	for j in range(1, len(arr)):
		key = arr[j]
		# Insert A[j] into the sorted sequence
		# A[0.....j]
		i = j - 1
		while i >= 0 and arr[i] > key:
			arr[i + 1] = arr[i]
			i = i - 1
			arr[i + 1] = key 
			#print(arr)
	return (arr)


if __name__ == '__main__':
	""" Defines unsorted list
		call the insertion sort function
		and print sorted lists
	"""
	print("Running insertion sort...")
	A = [5, 2, 4, 6, 1, 3]
	B = [31, 41, 59, 26, 41, 58]
	C = [391, 441, 59, 236, 41, 58, 776]

	print('Unsorted Array A:', A)
	print('Unsorted Array B:', B)
	print('Unsorted Array B:', C)
	print("----------------------------------")
	print('Sorted Array A', insertion_sort(A))
	print('Sorted Array B:', insertion_sort(B))
	print('Sorted Array B:', insertion_sort(C))


#!/usr/bin/env python3

# insertion_sort.py
""" file contains a simple implementation 
	of the insertion sort algorithm.
"""


def insertion_sort_asc(arr=[]):
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
			# place key after the element just smaller
			# than it
			arr[i + 1] = key 
			#print(arr)
	return (arr)

def insertion_sort_desc(arr=[]):
	"""Sorts an unsorted list in nonincreasing order
		using the INSERTION SORT algorithm
		param: Unsorted list of numbers
		return: Sorted list of numbers non-descending
	"""
	for j in range(1, len(arr)):
		key = arr[j]
		# Insert A[j] into the sorted sequence
		# A[0.....j]
		i = j - 1
		while i >= 0 and arr[i] < key:
			arr[i + 1] = arr[i]
			i = i - 1
			# place key after the element just smaller
			# than it
			arr[i + 1] = key 
			#print(arr)
	return (arr)


if __name__ == '__main__':
	""" Defines unsorted list
		call the insertion sort function
		and print sorted lists
	"""
	print("Running insertion sort...")
	A = [5, 2, 4, 6, 1, 3, 5, 7, 9, 10, 0]
	
	print('Unsorted Array A:', A)
	print("-------------------------------------------")
	print('Sorted Array Ascending ', insertion_sort_asc(A))
	print("-------------------------------------------")
	print('Sorted Array Descending A:', insertion_sort_desc(A))


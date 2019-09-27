#!/bin/python3
"""
Insertion sort algorithm


input=5461

for i in input: 
	cmp i[1] with i [0]

i = 1,2.....4
	j = 0,1,,,,,3
		if a[i] > a[j]
			


"""
# def swap(a,b):
# a
import timeit
import random_data_generator as rd


# def insertion_sort_On2(unsorted_list):
# 	for i in range(len(unsorted_list)):
# 		for j in range(len(unsorted_list)):
# 			key = unsorted_list[j]
# 			if key > unsorted_list[i]:
# 				unsorted_list[j] = unsorted_list[i]
# 				unsorted_list[i] = key
# 	return unsorted_list

def insertion_sort(input_list):
	n = len(input_list)
	for j in range(1, n):
		key = input_list[j]
		i = j-1
		while i > -1 and input_list[i] > key:
			input_list[i+1] = input_list[i]
			i -= 1
		input_list[i+1] = key
	return input_list

# def insertion_sort(unsorted_list):
# 	for i in range(1, len(unsorted_list)):
# 		j = i-1
# 		key = unsorted_list[i]
# 		while unsorted_list[j] > key and j > -1:
# 			unsorted_list[i] = unsorted_list[j]
# 			unsorted_list[j] = key
# 			j -= 1

# 		# for j in range(len(unsorted_list)):
# 		# 	key = unsorted_list[j]
# 		# 	if key > unsorted_list[i]:
# 		# 		unsorted_list[j] = unsorted_list[i]
# 		# 		unsorted_list[i] = key
# 	return unsorted_list


input_list = [5,20,42,6,1,3]

print("out ---> ", insertion_sort(input_list))

#print("out ---> ", insertion_sort_On2(rd.random_data_generator(1000)))




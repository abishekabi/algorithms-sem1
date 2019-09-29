#!/bin/python3
"""
Insertion sort algorithm

"""

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


def main(input_list):
	return insertion_sort(input_list)

if __name__ == "__main__":
	import random_data_generator as rd
	input_list = rd.random_data_generator(100)
	print("Input array --> \n", input_list)
	print("-" * 100)
	output_list = main(input_list)
	print("Insertion Sort Inplace version sorted array --> \n", output_list)



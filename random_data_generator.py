""" 
Generate random data for testing
"""

def random_data_generator(data_range = 1000):
	import random
	output_list = []
	for i in range(data_range):
		output_list.append(random.randint(1, data_range))
	return output_list 

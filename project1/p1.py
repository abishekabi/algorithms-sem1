"""
    Execution Time of sorting algorithms w.r.t input size
"""

import insertion_sort, merge_sort, \
    heap_sort, quick_sort_inplace, \
        quick_sort_modified
import timeit, time
# Random number generator
import random_data_generator as rd
import sys
sys.setrecursionlimit(100000)

global input_size, input_list, algorithm_type, algorithm_performance_time

algorithm_performance_time = []

def time_measure():
    algorithm_type.main(input_list)

if __name__ == "__main__":
    input_sizes = (1000, 2000, 4000, 5000, 10000, 40000, 50000)
    algorithm_types = [ insertion_sort, merge_sort, \
        heap_sort, quick_sort_modified, quick_sort_inplace]
    
    # measure perforance         
    for input_size in input_sizes[4:5]:
        input_list = rd.random_data_generator(input_size)
        # sorted array
        #input_list = [x for x in range(input_size)]
        # reverse sorted array
        #input_list = [x for x in range(input_size, 0, -1)]
        for algorithm_type in algorithm_types:
            # number = x where the higher the value of x, \
            # higher the accuracy of code execution time calcualation
            x= timeit.timeit(time_measure, number=1)
            d= { 
                "algo_type": algorithm_type.__name__,
                "input_size": input_size,
                "exec_time": x }
            algorithm_performance_time.append(d)
            time.sleep(2)
            
            
    print(algorithm_performance_time)

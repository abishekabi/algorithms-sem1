"""
    Comparision of sorting algorithms
"""

import insertion_sort, merge_sort, heap_sort, quick_sort_inplace, quick_sort_modified
import timeit
# Random number generator
import random_data_generator as rd


def time_measure():
    import insertion_sort, random_data_generator as rd 
    input_sizes = (1000, 2000, 4000, 5000, 10000, 40000, 50000)
    for input_size in input_sizes[:1]:
        input_size, input_list = input_size, rd.random_data_generator(input_size)


if __name__ == "__main__":
    # input_sizes = (1000, 2000, 4000, 5000, 10000, 40000, 50000)
    # for input_size in input_sizes[:1]:
    #     main(input_size, rd.random_data_generator(input_size))
    SETUP = """from __main__ import time_measure"""
    MAIN_CODE = """insertion_sort.main(input_list)"""

    x= timeit.timeit(
        setup=SETUP,
        stmt=MAIN_CODE,
        number=1
        )
    print(x)
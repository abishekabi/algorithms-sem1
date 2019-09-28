"""
Inplace Quick Sort

"""


def partition(S, p):
    '''
        S:input array , p: pivot
        3 partitions-> L, M, H
    '''
    L = []
    M = []
    H = []
    x = S.pop(p)
    while S:
        # Remove first element
        y = S.pop(0)
        if y < x:
            L.append(y)
        elif y == x:
            M.append(y)
        # condition y > x
        else:
            H.append(y)
    return L, M, H

def partition_inplace(S, low, high):
    """ 
    pivot: consider last element 
    """
    i = low
    pivot = S[high]
    for j in range(low, high):
        if S[j] < pivot:
            S[i], S[j] = S[j], S[i]
            i += 1
    S[i], S[high] = S[high], S[i]  
    return i
    # i = 1
    # j = len(S) - 1
    # for 
    # while i < j:
    #     if S[i] < p and S[j] > p:
    #         S[i], S[j] = S[j], S[i]
    #         i += 1
    #         j -= 1
    #     if S[i] < p:

    #         j -= 1
    #     if S[j] > p:
    #         i += 1
        
    #     i += 1
    #     j -= 1
    # return S




def quick_sort_inplace(S, low, high):
    if low < high:
        index = partition_inplace(S, low, high)
        # Recursion 
        quick_sort_inplace(S, low, index-1)
        quick_sort_inplace(S, index+1, high)
    return S

def main(input_list):
    # Initialize for first time
    start = 0
    end = len(input_list)-1
    output_list = quick_sort_inplace(input_list, start, end)
    print("Quick Sort Inplace version sorted array --> \n", output_list)


if __name__ == "__main__":
    #input_list = [ 7, 34, 5, 8, 3, 6, 2, 1, 6, 9]
    import random_data_generator as rd
    input_list = rd.random_data_generator()
    main(input_list)
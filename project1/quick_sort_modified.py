"""
Modified Quicksort

"""

def insertion_sort(S):
    n = len(S)
    for j in range(1, n):
        key = S[j]
        i = j-1
        while i > -1 and S[i] > key:
            S[i+1] = S[i]
            i -= 1
        S[i+1] = key
    return S


def median_of_three(S, start, end):
    mid = (start+end)//2
    if S[mid] < S[start]:
        S[mid], S[start] = S[start], S[mid]
    if S[end] < S[start]:
        S[end], S[start] = S[start], S[end]
    if S[end] < S[mid]:
        S[end], S[mid] = S[mid], S[end]
    S[mid], S[end-1] = S[end-1], S[mid]
    return S, S[end-1]

def partition_modified(S, start, end, pivot):
    i = start
    j = end-1
    while True:
        i += 1
        while (S[i] < pivot):
            i += 1
        j -= 1
        while (S[j] > pivot):
            j -= 1
        if (i < j):
            S[i], S[j] = S[j], S[i]
        else:
            break
    S[i], S[end-1] = S[end-1], S[i] 
    return S, i


def quick_sort_modified(S, start, end):
    if (start + 10) <= end:
        S, pivot = median_of_three(S, start, end)
        S, i = partition_modified(S, start, end, pivot)
        x = i - 1
        y = i + 1
        quick_sort_modified(S, start, x)
        quick_sort_modified(S, y, end)
        return S
    else:
        S = insertion_sort(S)
        return S

def main(input_list):
    # Initialize for first time
    start = 0
    end = len(input_list)-1
    return quick_sort_modified(input_list, start, end)

if __name__ == "__main__":
    import random_data_generator as rd
    #input_list = [7, 34, 5, 8, 3, 6, 2, 1, 6, 9, 10]
    input_list = rd.random_data_generator()
    output_list = main(input_list)
    print("Quick Sort Modified version sorted array --> \n", output_list)

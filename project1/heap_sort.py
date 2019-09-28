"""
Min-Heap construction

"""

def remove_from_heap(H):
    n = len(H) - 1
    removed_element = H[1]
    H[1] = H[n]
    # Remove the last element after copying
    H.pop()
    n = n - 1
    i = 1
    while i < n:
        # if node has 2 internal children
        if (2*i + 1) <= n:
            if H[i] <= H[2*i] and H[i] <= H[2*i +1]:
                return removed_element, H
            else:
                if H[2*i] < H[2*i +1]:
                    j = 2*i
                else:
                    j = 2*i + 1
                H[i], H[j] = H[j], H[i]
                i = j
        # This Node has zero or one internal children
        else:
            # This node has only one internal child or a last node
            if(2*i <= n):
                if H[i] > H[2*i]:
                    H[i], H[2*i] = H[2*i], H[i]
                return removed_element, H
            #i = 1
            break
    return removed_element, H
                
  
        # if H[2*i + 1] < H[i]:
        #     temp = H[2*i + 1]
        #     H[2*i + 1] = H[i]
        #     H[i] = temp
        # #Left child
        # if H[2*i] < H[i]:
        #     temp = H[2*i]
        #     H[2*i] = H[i]
        #     H[i] = temp
        # i = 2*i + 1
    # return removed_element, H

def insert_to_heap(H, e):
    H.append(e)
    n = len(H)
    i = n - 1
    while i > 1 and H[i] < H[i//2]:
        H[i], H[i//2] = H[i//2], H[i]
        i = i//2 
    return H

def heap_sort(input_list):
    H = []
    H.append(None)
    # Build a min heap
    for e in input_list:
        H = insert_to_heap(H, e)
    #return H
    sorted_list = []
    for _ in range(len(input_list)):
        removed_element, H = remove_from_heap(H)
        sorted_list.append(removed_element)
    return sorted_list

def main(input_list):
    return heap_sort(input_list)


if __name__ == "__main__":
    #input_list = [ 7, 34, 5, 8, 3, 6, 2, 1, 6, 9]
    import random_data_generator as rd
    input_list = rd.random_data_generator()
    output_list = main(input_list)
    print("HeapSort Inplace version sorted array --> \n", output_list)
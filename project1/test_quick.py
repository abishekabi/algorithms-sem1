def insertion_sort(a,low,high):
    for ele in range(low+1,high+1):
        key = a[ele]
        j = ele-1
        while(j>=0 and key < a[j]):
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

def decide_algo(a,low,high):
   if(low + 10 <= high): 
      if low<high:
          piv = partition(a,low,high)
          decide_algo(a,low,piv-1)
          decide_algo(a,piv+1,high)
   else:
      insertion_sort(a,low,high)

def quicksort(a,low,high):
   decide_algo(a,low,high)
   return a

def median(a, low, high, median):
  if a[low] < a[high]:
     
    return high if a[high] < a[median] else median
  else:
    return low if a[low] < a[median] else median

def partition(a,low,high):
   pindex = median(a, low, high, (low + high) // 2)
   a[low], a[pindex] = a[pindex], a[low]
   pivot = a[low]
   
   left = low
   right = high
   
   flag = False
   while not flag:
       while left <= right and a[left] <= pivot:
           left = left + 1

       while a[right] >= pivot and right >= left:
           right = right -1

       if right < left:
           flag = True
       else:
           a[left],a[right] =a[right],a[left]

   temp = pivot
   a[a.index(pivot)] = a[right]
   a[right] = temp
  
   return right

def main(input_list):
    # Initialize for first time
    start = 0
    end = len(input_list)-1
    return quicksort(input_list, start, end)


if __name__ == "__main__":    
    import random_data_generator as rd
    #input_list = [7, 34, 5, 8, 3, 6, 2, 1, 6, 9, 10]
    input_list = rd.random_data_generator(100)
    print("Input array --> \n", input_list)
    print("-" * 100)
    output_list = quicksort(input_list, 0, len(input_list)-1)
    print("Quick Sort Modified version sorted array --> \n", output_list)

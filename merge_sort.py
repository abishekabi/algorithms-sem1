"""
Merge sort algorithm

"""

def merge(S, S1, S2):
	#print(S, S1, S2)
	i = j = k = 0
	while i < len(S1) and j < len(S2):
		if ( S1[i] < S2[j] ):
			S[k] = S1[i]
			i += 1
		else:
			S[k] = S2[j]
			j += 1
		k += 1
	while i < len(S1): 
		S[k] = S1[i] 
		i+=1
		k+=1
		
	while j < len(S2): 
		S[k] = S2[j] 
		j+=1
		k+=1

	return S



def merge_sort(S):
	n = len(S)
	if( n > 1 ):
		low = 0
		high = n
		mid = (low+high)//2  
		if (low < high):
			S1 = S[0: mid]
			S2 = S[mid: ]
			merge_sort(S1)
			merge_sort(S2)
			return merge(S, S1, S2)

S = [5,6,4,9,1,3]



print("out ---> ", merge_sort(S))
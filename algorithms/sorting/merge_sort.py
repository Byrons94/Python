def merge(arr, left_index, mid_index, right_index):
    #left and right arrays
    left_array = arr[left_index:mid_index+1]
    right_array = arr[mid_index+1:right_index+1]
    
    #getting left and right array lenght
    left_array_length = mid_index - left_index + 1
    right_array_length = right_index - mid_index
    
    #indexes for mergin 2 arrays
    i = j = 0
    
    #index for array elements replacement
    k = left_index
    
    ## iterating over the two sub-arrays
    while i < left_array_length and j < right_array_length:

        ## comapring the elements from left and right arrays
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

	## adding remaining elements from the left and right arrays
    while i < left_array_length:
        arr[k] = left_array[i]
        i += 1
        k += 1

    while j < right_array_length:
        j += 1
        k += 1

def merge_sort(arr, left_index, right_index):
    ## base case for recursive function
    if left_index >= right_index:
        return
    
    #finding middle index
    mid_index = (left_index + right_index) // 2
    
    #recursive calls
    merge_sort(arr, left_index, mid_index)
    merge_sort(arr, mid_index + 1, right_index)
    
    #mergin sub arrays
    merge(arr, left_index, mid_index, right_index)
 
    
if __name__ == '__main__':
	## array initialization
	arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
	merge_sort(arr, 0, 8)

	## printing the array
	print(str(arr))    
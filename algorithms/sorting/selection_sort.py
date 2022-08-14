def selection_sort(arr, n):
    for i in range(n):
        ## to store the index of the minimum element
        min_element_index = i
        
        for j in range(i + 1, n):
            #checking and replacing minimun index
            if arr[j] < arr[min_element_index]:
                min_element_index = j
            
        #swapping the current element with minimun element
        arr[i], arr[min_element_index] = arr[min_element_index], arr[i]
        
if __name__ == '__main__':
    ## array initialization
	arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
	selection_sort(arr, 9)

	## printing the array
	print(str(arr))
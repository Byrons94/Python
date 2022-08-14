def bubble_sort(arr, n):
    for i in range(n):
        
        ## iterating from 0 to n-i-1 as last i elements are already sorted
        for j in range(n -i -1):
            ## checking the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                
if __name__ == '__main__':
	## array initialization
	arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
	bubble_sort(arr, 9)

	## printing the array
	print(str(arr))
 
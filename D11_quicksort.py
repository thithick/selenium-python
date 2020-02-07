# https://stackabuse.com/quicksort-in-python/

# Quicksort Sort

# pivot:  last element
# all smaller than pivot is left of pivot
# all greater than pivot is right of pivot
def partition(arr,low,high):
	i = ( low-1 )		 # index of smaller element
	pivot = arr[high]	 # pivot
	print('index of smaller element: ',i)
	print('pivot: ', pivot)
	print('low: ', low)
	print('high: ', high)
	for j in range(low , high):
		print('interation:',j)

		# If current element is smaller than the pivot
		if arr[j] < pivot:
			# increment index of smaller element
			i = i+1
			print("swaping : ",i,j)
			arr[i],arr[j] = arr[j],arr[i]


	arr[i+1],arr[high] = arr[high],arr[i+1]
	print('return value:',i+1)
	return ( i+1 )

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort
def quickSort(arr,low,high):
	if low < high:
		# pi is partitioning index, arr[p] is now at right place
		pi = partition(arr,low,high)

		# Separately sort elements before
		# partition and after partition
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)


# Driver code to test above
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
print("length of the given array: ",n)
quickSort(arr,0,n-1)
print ("Sorted array is:")
lst=[]
for i in range(n):
	lst.append(arr[i])
	# print ("%d" %arr[i])
print("final list: ", lst)

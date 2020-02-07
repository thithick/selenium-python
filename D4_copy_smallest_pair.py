# Python3 program to prints first k pairs with least sum from two
# arrays.

import sys
# Function to find k pairs with least sum such
# that one elemennt of a pair is from arr1[] and
# other element is from arr2[]
def kSmallestPair(arr1, n1, arr2, n2, k):
	if (k > n1*n2):
		print("k pairs don't exist")
		return

	# Stores current index in arr2[] for
	# every element of arr1[]. Initially
	# all values are considered 0.
	# Here current index is the index before
	# which all elements are considered as
	# part of output.
	index2 = [0 for i in range(n1)]

	while (k > 0):
		# Initialize current pair sum as infinite
		min_sum = sys.maxsize
		min_index = 0

		# To pick next pair, traverse for all elements
		# of arr1[], for every element, find corresponding
		# current element in arr2[] and pick minimum of
		# all formed pairs.
		for i1 in range(0,n1,1):
			# Check if current element of arr1[] plus
			# element of array2 to be used gives minimum
			# sum
			if (index2[i1] < n2 and arr1[i1] + arr2[index2[i1]] < min_sum):
				# Update index that gives minimum
				min_index = i1

				# update minimum sum
				min_sum = arr1[i1] + arr2[index2[i1]]

		print("(",arr1[min_index],",",arr2[index2[min_index]],")",end = " ")

		index2[min_index] += 1

		k -= 1

# Driver code
if __name__ == '__main__':
	# arr1 = [1, 3, 11]
	arr1 = [1, 1, 2]
	n1 = len(arr1)

	# arr2 = [2, 4, 8]
	arr2 = [1, 2, 3]
	n2 = len(arr2)

	k = 2
	kSmallestPair( arr1, n1, arr2, n2, k)

# This code is contributed by
# Shashank_Sharma

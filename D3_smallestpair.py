# program to prints first k pairs with least sum from two arrays.
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

import sys

def kSmallestPair(arr1, arr2, k):
	n1 = len(arr1)
	n2 = len(arr2)
	if (k > n1*n2):
		print("k pairs don't exist")
		return
	# create an empty list which has n1 number of 0s
	# list comprehension basic syntax: [ expression for item in list if conditional ]
	index2 = [0 for i in range(n1)]
	print (index2)
	while (k > 0):
		# Initialize current pair sum as infinite
		print(k)
		min_sum = sys.maxsize
		min_index = 0
		print("min_sum",min_sum)
		print("min_index",min_index)

		# To pick next pair, traverse for all elements
		# of arr1[], for every element, find corresponding
		# current element in arr2[] and pick minimum of
		# all formed pairs.
		for j in range(0,n1,1):
			# Check if current element of arr1[] plus
			# element of array2 to be used gives minimum
			# sum
			# print("index2",index2)
			print("index2[j]",index2[j])
			if (index2[j] < n2 and arr1[j] + arr2[index2[j]] < min_sum):
				# Update index that gives minimum
				min_index = j

				# update minimum sum
				min_sum = arr1[j] + arr2[index2[j]]

		print("(",arr1[min_index],",",arr2[index2[min_index]],")",end = " ")

		index2[min_index] += 1

		k -= 1

# Driver code
if __name__ == '__main__':
	# arr1 = [1, 3, 11]
	# arr2 = [2, 4, 8]
	arr1 = [1, 1, 2]
	arr2 = [1, 2, 3]

	k = 4
	kSmallestPair( arr1, arr2, k)

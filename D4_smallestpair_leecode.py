# program : prints first k pairs with least sum from two lists.
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

#to assume the max value of the minimum sum of pair I am going to use maxsize. which is from the python standard library sys
#so importing sys
import sys

# this is the function name for this program, where lst1,lst2,k are the parameters
# lst1 for the first list, lst2 for the second list, k is for number of pairs
def kSmallestPair(lst1, lst2, k):
	# get the length of list1 and list2
	n1 = len(lst1)
	n2 = len(lst2)
	# just to capture list out of bound error message.
	# if any of the list is empty we just stop the test
	if (n1*n2==0):
		print("list is empty ")
		return
	# if the total number of pair(n1*n2) is less than K pairs that resetting the K value to n1*n2
	if (k > n1*n2 and n1*n2!=0):
		print("k pairs don't exist, so getting the maximum pairs")
		k=n1*n2
		print("total K pairs are: ",k)

	# this is to set the minimum index to the list2 elements, when sum of the apirs are minimum
	lst2index=[0 for i in range (n1)]
	# since the output is expected in list format, I am going to define and use this list variable
	finallst=[]
	# you can use for loop or while loop, Since we know the value of K, I am going to use for loop
	for k in range (k,0,-1):
	# while (k>0): #you can also use while loop
		# this is like a pivot variable, I just used to setup the maxsize. since we do not know the range of the values in the list
		min_sum=sys.maxsize
		# initializing the minimum index value
		min_index=0
		# for loop to traverse from first list to second list
		for i in range(0,n1,1):
			# this is the condition that we want to make sure.
			# lst2index is for list2 index for earch elements. lst2index[i]<n2 = the capture "list index out of range" message
			if(lst2index[i]<n2 and lst1[i]+lst2[lst2index[i]]<min_sum):
				# set the minimum index value, so this will update for list2 index.
				min_index=i
				# set the minimum sum value. so the minimum sub value will be reset for each iteration.
				min_sum=lst1[i]+lst2[lst2index[i]]
		# we are going to use the lst variable to store the minimum pairs in an array
		lst=[]
		# append the first value of the minimum pairs
		lst.append(lst1[min_index])
		# append the second value of the minimum pairs
		lst.append(lst2[lst2index[min_index]])
		# append the list apirs into another final list
		finallst.append(lst)
		# increment list2 indexs
		lst2index[min_index]+=1
		# k-=1 #only if you are using while loop
	# Print the finale list (stdout)
	print(finallst)
	# print the final output (Output)
	return finallst


# this is the driver code
if __name__ == '__main__':
	lst1 = [1, 1, 2]
	lst2 = [1, 2, 3]
	k = 2
	kSmallestPair( lst1, lst2, k)

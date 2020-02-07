# program to prints first k pairs with least sum from two lists.

import sys

def kSmallestPair(lst1, lst2, k):
	n1 = len(lst1)
	n2 = len(lst2)
	if (k > n1*n2):
		print("k pairs don't exist")
		return

	# for j in range(0,n1):
	# 	for i in range(0,n2):
	# 		print("(",lst1[j],",",lst2[i],")",end = " ")
	# 		# print("[",lst1[j],",",lst2[i],"]")

	lst2index=[0 for i in range (n1)]
	print(lst2index)
	while (k>0):
		min_sum=sys.maxsize
		min_index=0
		for i in range(0,n1,1):
			if(lst2index[i]<n2 and lst1[i]+lst2[lst2index[i]]<min_sum):
				min_index=i
				min_sum=lst1[i]+lst2[lst2index[i]]
		print("(",lst1[min_index],",",lst2[lst2index[min_index]],")",end=" ")
		lst2index[min_index]=lst2index[i]+1
		k=k-1



# Driver code
if __name__ == '__main__':
	# lst1 = [1, 3, 11]
	# lst2 = [2, 4, 8]
	lst1 = [1, 1, 2]
	lst2 = [1, 2, 3]

	k = 2
	kSmallestPair( lst1, lst2, k)

# D10_max_sum_knagations.py
# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations
# Input: A = [4,2,3], K = 1
# Output: 5
# Explanation: Choose indices (1,) and A becomes [4,-2,3].

def maxsumK(strlist,K):
    # n=len(A)
    # print(n)
    #
    # st=set(A)
    # print(st)
    intlist = map(int, strlist)  # list(map(int, strlist)) on Python 3
    print(intlist)
    quicksort(intlist)
    print(intlist)







if __name__ == '__main__':
    A = [4,2,3,0,-1]
    K = 1
    # Possibly read from file as list of string
    strlist = ['35', '-1', '-2', '-7', '-8', '-3', '-4', '20', '-6', '53']

    maxsumK(strlist, K)

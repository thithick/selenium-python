# PASS:
# https://leetcode.com/articles/two-sum/
# 1. Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


def twoSum(nums, target):
    n=len(nums)
    # print(n)
    for i in range(n):
        for j in range(n):
            # print(i,j)
            if (i!=j and nums[i]+nums[j]==target):
                lst=[]
                lst.append(i)
                lst.append(j)
                print(lst)
                return lst

if __name__ == '__main__':
    # nums=[0,7,9,2,22]
    # nums=[3,2,3]
    # target=6
    nums=[2,5,5,11]
    target=10
    twoSum(nums, target)

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such 
that each unique element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in 
the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for i, item in enumerate(nums):
            if i != len(nums)-1:
                if nums[i+1] == item:
                    #without_duplicates = set(nums[i+1:])
                    nums[i:] = list(set(nums[i+1:]))
        nums.sort()
        return len(nums)
    
nums = [0,0,1,1,1,2,2,3,3,4]

Solution.removeDuplicates(nums)
print(nums)
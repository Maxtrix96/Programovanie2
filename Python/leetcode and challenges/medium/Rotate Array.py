"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
from collections import deque

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_nums = deque(nums)
        new_nums.rotate(k)
        nums[0:len(nums)+1] = new_nums

nums = [1,2,3,4,5,6,7]
k = 3

thingy = Solution()
thingy.rotate(nums, k)
print(nums)
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume 
that the majority element always exists in the array.
"""

class Solution:
    #@staticmethod
    #def majorityElement(nums: list[int]) -> int:
    def majorityElement(self, nums: list[int]) -> int:
        item_dict = {item: 0 for item in set(nums)}
        for item in nums:
            item_dict[item] += 1 
        highest = max(item_dict.values())
        print(highest)
        return list(item_dict.keys())[list(item_dict.values()).index(highest)]

nums = [1,1,2,2]
thingy = Solution()
print(thingy.majorityElement(nums))
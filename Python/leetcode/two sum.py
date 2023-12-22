class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]: # O(n^2)
        for i, num in enumerate(numbers):
            dif = target - num
            if dif in numbers:
                if i == numbers.index(dif):
                    pass
                else:
                    return [i, numbers.index(dif)]
        return False

    
first = Solution()
print("First: ", first.twoSum([2,7,11,15], 9))

second = Solution()
print("Second: ", second.twoSum([3, 2, 4], 6))

third = Solution()
print("Third: ", third.twoSum([3,3], 6))
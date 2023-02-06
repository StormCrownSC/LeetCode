class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] != 1:
                return nums[i] + 1
        return len(nums) if nums[0] == 0 else 0

"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.find(nums, target, 0)
        
        
    def find(self, arr, target, value):
        for elem in range(value + 1, len(arr)):
            if arr[value] + arr[elem] == target:
                return (value, elem)
            
        return self.find(arr, target, value + 1) 
        
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

"""
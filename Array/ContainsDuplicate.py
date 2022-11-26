class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) != len(list(set(nums))):
            return True
        return False    


if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1,2,3,1]))
    print(s.containsDuplicate([1,2,3,4]))
    print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))

"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
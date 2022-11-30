class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        for index in range(len(nums)):
            if nums[index + count] == 0:
                nums.append(nums.pop(index + count))
                count -= 1
        return nums


if __name__ == "__main__":
    s = Solution()
    print(s.moveZeroes([0,1,0,3,12]))
    print(s.moveZeroes([0]))
    print(s.moveZeroes([0, 0, 1]))
    print(s.moveZeroes([0,1,0,3,12]))


"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""
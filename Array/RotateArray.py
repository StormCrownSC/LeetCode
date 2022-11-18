class Solution(object):
    def rotate(self, nums, k):
        length = len(nums) - 1
        if 1 <= length + 1 <= 10**5 or 0 <= k <= 10**5:
            for i in range(k % len(nums)):
                nums.insert(0, nums.pop())
            return nums
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """


if __name__ == "__main__":
    s = Solution()
    print(s.rotate([1,2,3,4,5,6,7], 3))
    print(s.rotate([-1,-100,3,99], 2))
    print(s.rotate([1,2,3,4,5], 4))

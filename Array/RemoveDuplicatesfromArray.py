class Solution(object):
    def removeDuplicates(self, nums):
        size = len(nums)
        insertIndex = 1
        for i in range(1, size):
            if nums[i - 1] != nums[i]:      
                nums[insertIndex] = nums[i] 
                insertIndex += 1       
        return insertIndex

if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([1,1,2]))
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(s.removeDuplicates([0,1]))

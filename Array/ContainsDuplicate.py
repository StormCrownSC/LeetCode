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
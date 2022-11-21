class Solution(object):
    def singleNumber(self, nums):
        new_nums = set()
        all_nums = set()
        for elem in nums:
            if elem in new_nums:
                all_nums.add(elem)
            else:
                new_nums.add(elem)
        return new_nums - all_nums


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([1,2,3,1]))
    print(s.singleNumber([1,2,3,4]))
    print(s.singleNumber([1,1,1,3,3,4,3,2,4,2]))
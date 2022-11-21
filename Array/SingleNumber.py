class Solution(object):
    def singleNumber(self, nums):
        new_nums = set()
        all_nums = set()
        for elem in nums:
            if elem in new_nums:
                all_nums.add(elem)
            else:
                new_nums.add(elem)
        print(new_nums, all_nums)
        return list(new_nums - all_nums)[0]


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([2,2,1]))
    print(s.singleNumber([4,1,2,1,2]))
    print(s.singleNumber([1]))
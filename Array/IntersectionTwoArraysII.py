class Solution(object):
    def intersect(self, nums1, nums2):
        new_nums = []
        for elem in nums1:
            if elem in nums2 and nums1.count(elem) >= new_nums.count(elem) + 1 and nums2.count(elem) >= new_nums.count(elem) + 1:
                    new_nums.append(elem)
        return new_nums


if __name__ == "__main__":
    s = Solution()
    print(s.intersect([1,2,2,1], [2,2]))
    print(s.intersect([4,9,5], [9,4,9,8,4]))
    print(s.intersect([1,2,2,1], [2]))

"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        count = 0
        while True:
            for elem in range(1, len(strs)):
                if count >= len(strs[elem]) or count >= len(strs[0]) or strs[0][count] != strs[elem][count]:
                    return answer
            if count >= len(strs[0]):
                return answer
            answer += strs[0][count]
            count += 1
        
        return answer
        

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
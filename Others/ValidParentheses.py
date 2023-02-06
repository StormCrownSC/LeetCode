class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        check = {")": "(", "}": "{", "]": "["}
        for elem in s:
            if elem == "(" or elem == "{" or elem == "[":
                stack.append(elem)
            elif elem == ")" or elem == "}" or elem == "]":
                if len(stack) <= 0 or check[elem] != stack.pop():
                    return False
                
        return True if len(stack) == 0 else False

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""
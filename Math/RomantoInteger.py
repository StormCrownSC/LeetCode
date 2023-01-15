class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = list()
        answer = 0
        for num in s:
            numbers.append(self.convertor(num.upper()))
        for index, num in enumerate(numbers):
            if index > 0:
                if num <= numbers[index - 1]:
                    answer += num
                else:
                    answer = answer - numbers[index - 1] * 2 + num
                    
            else:
                answer += num
        return answer
    
    def convertor(self, num):
        if num == "I":
            return 1
        elif num == "V":
            return 5
        elif num == "X":
            return 10
        elif num == "L":
            return 50
        elif num == "C":
            return 100
        elif num == "D":
            return 500
        elif num == "M":
            return 1000
        return None

"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
"""
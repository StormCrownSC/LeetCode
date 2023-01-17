class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = list()
        for row in range(1, numRows + 1):
            answer.append(list())
            for elem in range(1, row + 1):
                if row >= 3 and 1 < elem < row:
                    answer[row-1].append(answer[row-2][elem-2] + answer[row-2][elem-1])
                else:
                    answer[row-1].append(1)
        return answer
        

"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""
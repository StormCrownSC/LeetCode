class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = [row[:] for row in matrix]

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = temp[len(matrix) - j - 1][i]

"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
"""
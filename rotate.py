from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates the image by 90 degrees (clockwise) in-place.
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # 1. Transpose the matrix
        # Swap elements across the main diagonal (i, j) <-> (j, i)
        # We only need to iterate over the upper triangle (j > i) to avoid double-swapping
        for i in range(n):
            for j in range(i + 1, n):
                # Python's tuple swapping is concise
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # 2. Reverse each row
        # This is equivalent to mirroring the matrix horizontally
        for i in range(n):
            matrix[i].reverse()
            
        # Example for a 3x3 matrix:
        # Initial:        Transpose:       Reverse Rows: (Final)
        # 1 2 3           1 4 7            7 4 1
        # 4 5 6     ->    2 5 8      ->    8 5 2
        # 7 8 9           3 6 9            9 6 3

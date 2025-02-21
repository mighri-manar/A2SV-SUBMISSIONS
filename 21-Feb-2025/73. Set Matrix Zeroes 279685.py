# Problem: 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """   
        lili=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    lili.append((i,j))
        for tup in lili:
            matrix[tup[0]]=[0]*len(matrix[0])

            for k in range(len(matrix)):
                matrix[k][tup[1]]=0

        
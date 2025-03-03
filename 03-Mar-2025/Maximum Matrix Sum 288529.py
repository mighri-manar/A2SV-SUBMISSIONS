# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        flattened = [val for row in matrix for val in row]
        total = sum(abs(val) for val in flattened)
        negative = sum(1 for val in flattened if val < 0)
        min_abs = min(abs(val) for val in flattened)
        
        return total- 2 * min_abs if negative % 2 else total
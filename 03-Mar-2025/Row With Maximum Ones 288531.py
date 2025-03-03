# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        idx = [row.count(1) for row in mat]
        max_count = max(idx)
        for i in range(len(mat)):
            if idx[i]==max_count:
                return [i, idx[i]]
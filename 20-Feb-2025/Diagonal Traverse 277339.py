# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        res=[]
        diag=defaultdict(list)
        m=len(mat) 
        n=len(mat[0])
        for i in range(m):
            for j in range(n):
                diag[i+j].append(mat[i][j])
        for k in sorted(diag.keys()):
            if k%2==0:
                res.extend(reversed(diag[k]))  
            else:
                res.extend(diag[k])  
        return res
# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
         m,n=len(image), len(image[0])
         new=[[0]*n for _ in range(m)]
         for i in range(m):
            for j in range(n):
                 if image[i][n-1-j]==0:
                    new[i][j]=1
                 else:
                    continue   
         return new
# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
         count=0
         g.sort()
         s.sort()
         greed, size=0,0
         while (greed< len(g) and size<len(s)):
             if g[greed]<=s[size]:
                count+=1
                size+=1
                greed+=1

             else :
                size+=1
         return count
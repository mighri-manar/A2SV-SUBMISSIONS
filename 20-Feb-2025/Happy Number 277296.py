# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
         sum_sqrt=n
         lili=list(str(n))
         encountered=set()
         encountered.add(n)
         while sum_sqrt!=1:
            sum_sqrt=sum(int(x)**2 for x in lili)
            lili=list(str(sum_sqrt))
            if sum_sqrt in encountered:
                 return False
            
            encountered.add(sum_sqrt)    
            
         return True
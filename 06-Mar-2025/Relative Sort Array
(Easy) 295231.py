# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
         count = Counter(arr1)  
         res = []
         for num in arr2:
             res.extend([num] * count[num])
             del count[num]  
         remain = sorted(count.elements()) 
         res.extend(remain)
    
         return res  
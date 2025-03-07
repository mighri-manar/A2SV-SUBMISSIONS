# Problem: Reduction Operations to Make the Array Elements Equal - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
         counter=Counter(nums)
         sorted_k = sorted(counter.keys())  
         total=0
         for idx, num in enumerate(sorted_k):
             total+=idx*counter[num]
         return total    
             
  
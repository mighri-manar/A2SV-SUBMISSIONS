# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
         new=['.']*len(s)
         for i, char in enumerate(s):
             new[indices[i]]=char
         return "".join(new)    
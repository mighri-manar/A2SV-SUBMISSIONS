# Problem: Third Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        h=list(set(nums))
        h.sort(reverse=True)
        return h[2] if len(h) >= 3 else h[0]
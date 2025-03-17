# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        append_idx = 0
        current_idx = 0
        while current_idx < len(nums):
            if nums[current_idx] != 0:
                nums[append_idx], nums[current_idx] = nums[current_idx], nums[append_idx]
                append_idx += 1  
            current_idx += 1 

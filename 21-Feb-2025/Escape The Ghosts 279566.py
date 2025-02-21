# Problem: Escape The Ghosts - https://leetcode.com/problems/escape-the-ghosts/

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        d_player = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            d_ghost = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if d_ghost <= d_player:
                return False
        return True
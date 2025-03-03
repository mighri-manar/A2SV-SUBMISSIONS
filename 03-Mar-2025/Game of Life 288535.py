# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        tmp = copy.deepcopy(board) 
        R = len(board)
        C = len(board[0])
        moves = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        for i in range(R):
            for j in range(C):
                voisins = 0
                for x,y in moves:          
                    if (0 <= i+x < R) and (0 <= j+y < C):                  
                        if tmp[i+x][j+y] == 1:
                            voisins += 1
                if board[i][j] == 1:
                    if voisins < 2 or voisins > 3: 
                        board[i][j] = 0
                    if voisins == 2 or voisins == 3:  
                        board[i][j] = 1
                elif board[i][j] == 0:
                    if voisins == 3:
                        board[i][j] = 1
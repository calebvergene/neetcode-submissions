class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col):
            if board[row][col] != 'O':
                return
            
            board[row][col] = 'T'

            for direction in directions:
                newr, newc = row + direction[0], col + direction[1]
                if newr in range(ROWS) and newc in range(COLS) and board[newr][newc] == 'O':
                    dfs(newr, newc)
                    
        # iterate through board
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS-1)
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS-1, c)
                
        # then, delete capturable cells
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'T':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'
                    
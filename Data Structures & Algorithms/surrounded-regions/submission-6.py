class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        ROWS, COLS = len(board), len(board[0])
        q = collections.deque()

        # multi source bfs from 0s on the border
        for c in range(COLS):
            if board[0][c] == "O":
                q.append((0, c))
            if board[ROWS-1][c] == "O":
                q.append((ROWS-1, c))
        for r in range(1, ROWS-1):
            if board[r][0] == "O":
                q.append((r, 0))
            if board[r][COLS-1] == "O":
                q.append((r, COLS-1))
        
        while q:
            row, col = q.popleft()
            board[row][col] = "N"
            for direction in directions:
                newr, newc = direction[0] + row, direction[1] + col
                if newr in range(ROWS) and newc in range(COLS) and board[newr][newc] == "O":
                    board[newr][newc] = "N"
                    q.append((newr, newc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "N":
                    board[r][c] = "O"
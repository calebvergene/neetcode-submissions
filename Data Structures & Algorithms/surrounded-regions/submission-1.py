class Solution:
    def solve(self, board: List[List[str]]) -> None:
        capture, cant_capture, temp = set(), set(), set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col):
            # return true if it can be captured
            nonlocal temp
            temp.add((row,col))

            # need to check if on border
            if row == 0 or row == ROWS-1 or col == 0 or col == COLS-1:
                capturable = False
            else:
                capturable = True

            for direction in directions:
                newr, newc = row + direction[0], col + direction[1]
                if newr in range(ROWS) and newc in range(COLS) and board[newr][newc] == 'O' and (newr, newc) not in capture.union(cant_capture).union(temp):
                    capturable = capturable and dfs(newr, newc)
            
            return capturable
        
        # iterate through board
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O' and (row,col) not in capture.union(cant_capture):
                    capturable = dfs(row, col)
                    if capturable:
                        capture = capture.union(temp)
                    else:
                        cant_capture = cant_capture.union(temp)
                    temp = set()
                
        # then, delete capturable cells
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in capture:
                    board[row][col] = 'X'
                    
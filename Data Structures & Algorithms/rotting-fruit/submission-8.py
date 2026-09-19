class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        # first, find rotten oranges and num of total oranges
        oranges_left, rotten = 0, []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    oranges_left += 1
                elif grid[r][c] == 2:
                    rotten.append([r,c])
        
        # multisource bfs
        q = deque(rotten)
        minutes = 0 
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for d in directions:
                    newr, newc = row+d[0], col+d[1]
                    if newr in range(ROWS) and newc in range(COLS) and grid[newr][newc] == 1:
                        grid[newr][newc] = 2
                        oranges_left -= 1
                        q.append([newr,newc])
            if q:
                minutes += 1
        
        return minutes if not oranges_left else -1
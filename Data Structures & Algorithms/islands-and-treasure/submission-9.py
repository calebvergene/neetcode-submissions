class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        # first, get coords of treasure chests
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
        
        # now bfs from each chest 
        distance = 0 
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                if distance:
                    grid[row][col] = distance
                for direction in directions:
                    newr, newc = row + direction[0], col + direction[1]
                    if newr in range(ROWS) and newc in range(COLS) and grid[newr][newc] == 2147483647:
                        grid[newr][newc] = 0
                        q.append([newr,newc])
            
            distance += 1
                
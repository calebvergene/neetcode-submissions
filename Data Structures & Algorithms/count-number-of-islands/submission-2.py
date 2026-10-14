class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        islands = 0

        def dfs(row, col):
            grid[row][col] = "0"

            for direction in directions:
                newr, newc = direction[0] + row, direction[1] + col
                if newr in range(ROWS) and newc in range(COLS) and grid[newr][newc] == "1":
                    dfs(newr, newc)
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col) # turn all the 1s to 0s
                    islands += 1
        
        return islands
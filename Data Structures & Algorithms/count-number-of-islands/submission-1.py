class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0 
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [-1,0], [0,-1]]

        def dfs(row, col):
            if grid[row][col] == '0':
                return 
            else:
                grid[row][col] = '0'
                for direction in directions:
                    newr, newc = row + direction[0], col + direction[1]
                    if newr in range(rows) and newc in range(cols):
                        dfs(newr, newc)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)
        
        return islands
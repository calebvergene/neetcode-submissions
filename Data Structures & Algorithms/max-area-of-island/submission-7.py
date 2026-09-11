class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0 
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        def dfs(row, col) -> int:
            if grid[row][col] == 0:
                return 0
            area = 1
            grid[row][col] = 0
            for direction in directions:
                newr, newc = row + direction[0], col + direction[1]
                if newr in range(rows) and newc in range(cols):
                    area += dfs(newr, newc)

            return area
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_island = max(max_island, dfs(row, col))
        
        return max_island
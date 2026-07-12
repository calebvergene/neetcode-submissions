class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))
            area = 0
            while q:
                row, col = q.popleft()
                area += 1
                grid[row][col] = 0
                for direction in directions:
                    if (row + direction[0] in range(rows) and col + direction[1] in range(cols)
                    and grid[row + direction[0]][col + direction[1]] == 1):
                        q.append((row + direction[0], col + direction[1]))
            nonlocal max_area
            max_area = max(max_area, area)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    bfs(r, c)
        
        return max_area
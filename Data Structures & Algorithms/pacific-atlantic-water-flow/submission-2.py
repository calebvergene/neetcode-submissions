class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # bfs from borders then go in. thats how we know if it "reached water"
        pacific, atlantic = set(), set()
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        # set up bfs
        pq, aq = deque(), deque()
        for r in range(ROWS):
            pq.append([r, 0])
            pacific.add((r, 0))
            aq.append([r, COLS-1])
            atlantic.add((r, COLS-1))
        for c in range(COLS):
            pq.append([0, c])
            pacific.add((0, c))
            aq.append([ROWS-1, c])
            atlantic.add((ROWS-1, c))
                
        # find pacific then atlantic
        def bfs(queue, reach):
            while queue:
                row, col = queue.popleft()
                for direction in directions:
                    newr, newc = row + direction[0], col + direction[1]
                    if newr in range(ROWS) and newc in range(COLS) and (newr,newc) not in reach and heights[newr][newc] >= heights[row][col]:
                        reach.add((newr,newc))
                        queue.append([newr,newc])

        bfs(pq, pacific)
        bfs(aq, atlantic)

        return list(pacific.intersection(atlantic))
        


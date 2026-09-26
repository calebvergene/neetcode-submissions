class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        # (row, col)
        squares = defaultdict(set)

        # then keep row set for each row
        for r in range(len(board)):
            curr_row = set()
            for c in range(len(board[0])):
                num = board[r][c]
                if num == '.':
                    continue
                
                if num in cols[c]:
                    return False
                cols[c].add(num)
                if num in curr_row:
                    return False
                curr_row.add(num)
                square = (r//3, c//3)
                if num in squares[square]:
                    return False
                squares[square].add(num)

        return True
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)
        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    continue
                if (board[x][y] in rows[y] or board[x][y] in columns[x] or board[x][y] in squares[(x//3,y//3)]):
                    return False
                rows[y].add(board[x][y])
                columns[x].add(board[x][y])
                squares[(x//3,y//3)].add(board[x][y])
        return True
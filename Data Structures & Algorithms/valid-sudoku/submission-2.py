class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    continue
                if board[x][y] in rows[x] or board[x][y] in columns[y] or board[x][y] in boxes[(x//3, y//3)]:
                    return False
                rows[x].add(board[x][y])
                columns[y].add(board[x][y])
                boxes[(x//3, y//3)].add(board[x][y])
        return True
                

        


            
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        columns=defaultdict(set)
        grids=defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col]==".":
                    continue
                else:
                    if board[row][col] in rows[row] or board[row][col] in columns[col] or board[row][col] in grids[(row//3,col//3)]:
                        return False
                    rows[row].add(board[row][col]) 
                    columns[col].add(board[row][col]) 
                    grids[(row//3,col//3)].add(board[row][col]) 
    
        return True
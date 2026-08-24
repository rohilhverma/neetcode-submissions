class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = defaultdict(set)
        c = defaultdict(set)
        b = defaultdict(set)
        for x in range(len(board)):

            for y in range(len(board[x])):
                if board[x][y]==".":
                    continue
                elif board[x][y] in r[x]:
                    return False
                elif board[x][y] in c[y]:
                    return False
                elif board[x][y] in b[(x//3,y//3)]:
                    return False
                else:
                    r[x].add(board[x][y])
                    c[y].add(board[x][y])
                    b[(x//3,y//3)].add(board[x][y])
        return True
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited, safe = set(), set()
        def dfs(x, y, visited, safe):
            if x < 0 or y < 0 or x == len(board) or y == len(board[0]) or (x, y) in visited or board[x][y] == "X":
                return False

            if board[x][y] == "O" and (x, y) not in visited:
                safe.add((x, y))

            visited.add((x, y))
            dfs(x+1,y,visited,safe)
            dfs(x-1,y,visited,safe)
            dfs(x,y+1,visited,safe)
            dfs(x,y-1,visited,safe)

        for x in range(len(board)):
            if x == 0 or x == len(board)-1:
                for y in range(len(board[0])):
                    if board[x][y] == "O":
                        dfs(x, y, visited,safe)
                    visited.add((x,y))
            else:
                """run the dfs on the first and last val of each row"""
                if board[x][0] == "O": 
                    dfs(x,0,visited,safe)
                if board[x][-1] == "O":
                    dfs(x,len(board[x])-1,visited,safe)
                visited.add((x,0))
                visited.add((x,len(board[x])-1))



        for x in range(len(board)):
            for y in range(len(board[x])):
                if (x,y) in visited:
                    continue
                board[x][y] = "X"
        
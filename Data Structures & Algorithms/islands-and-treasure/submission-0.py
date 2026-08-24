from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        direc = [[0,-1],[0,1],[-1,0],[1,0]]
        visited=set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    q.append((x,y))
                    visited.add((x,y))
        while q:
            for _ in range(len(q)):
                curr=q.popleft()
                for x, y in direc:
                    if curr[0] + x < 0 or curr[1] + y < 0 or curr[0] + x == len(grid) or curr[1] + y == len(grid[0]) or grid[curr[0]+x][curr[1]+y]==-1 or (curr[0]+x,curr[1]+y) in visited:
                        continue
                    grid[curr[0]+x][curr[1]+y] = grid[curr[0]][curr[1]] + 1
                    q.append((curr[0]+x,curr[1]+y))
                    visited.add((curr[0]+x,curr[1]+y))

            

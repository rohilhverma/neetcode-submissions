from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh=0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    q.append((x,y))
                elif grid[x][y] == 1:
                    fresh+=1
        direc = [[0,-1],[0,1],[1,0],[-1,0]]
        t=0
        if not fresh:
            return t
        while q:
            f=fresh
            for _ in range(len(q)):
                curr = q.popleft()
                for x, y in direc:
                    if curr[0] + x < 0 or curr[1] + y < 0 or curr[0] + x == len(grid) or curr[1] + y == len(grid[0]) or grid[curr[0]+x][curr[1]+y]==0 or grid[curr[0]+x][curr[1]+y]==2:
                        continue
                    grid[curr[0]+x][curr[1]+y]=2
                    fresh-=1
                    q.append((curr[0]+x,curr[1]+y))
            if f > fresh:
                t+=1
        if fresh:
            return -1
        return t

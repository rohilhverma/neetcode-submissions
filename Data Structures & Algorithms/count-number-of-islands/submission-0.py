class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited=set()
        def dfs(r, c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or (r,c) in self.visited or grid[r][c]=='0':
                return
            self.visited.add((r, c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
            return
        
        c=0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x,y) in self.visited:
                    continue
                elif grid[x][y] == '0':
                    self.visited.add((x,y))
                else:
                    dfs(x, y)
                    c+=1
        return c

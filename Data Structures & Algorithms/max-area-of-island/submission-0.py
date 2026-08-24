class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        self.visited=set()

        def dfs(r, c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or (r,c) in self.visited or grid[r][c] == 0:
                return 0 
            count=0
            self.visited.add((r,c))
            count+=dfs(r-1,c)
            count+=dfs(r+1,c)
            count+=dfs(r,c-1)
            count+=dfs(r,c+1)
            return 1 + count
        
        
        returnVal=0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]==1 and (x,y) not in self.visited:
                    returnVal = max(returnVal,dfs(x,y)) 
                else:
                    self.visited.add((x,y))
        return returnVal

                    
            
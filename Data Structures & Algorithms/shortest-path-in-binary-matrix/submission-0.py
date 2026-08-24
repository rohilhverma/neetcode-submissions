from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque()
        returnVal=101
        q.append([0,0,1])
        visited=set()
        while q:
            curr = q.popleft()
            if curr[0] < 0 or curr[1] < 0 or curr[0] >= len(grid) or curr[1] >= len(grid[0]) or (curr[0], curr[1]) in visited or grid[curr[0]][curr[1]] == 1:
                continue
            elif curr[0] == len(grid[0])-1 and curr[1] == len(grid[0])-1:
                returnVal = min(returnVal, curr[2])
            visited.add((curr[0],curr[1]))

            q.append([curr[0]+1,curr[1],curr[2]+1])
            q.append([curr[0]-1,curr[1],curr[2]+1])
            q.append([curr[0],curr[1]+1,curr[2]+1])
            q.append([curr[0],curr[1]-1,curr[2]+1])
            q.append([curr[0]+1,curr[1]+1,curr[2]+1])
            q.append([curr[0]-1,curr[1]-1,curr[2]+1])
            q.append([curr[0]+1,curr[1]-1,curr[2]+1])
            q.append([curr[0]-1,curr[1]+1,curr[2]+1])
            


        if returnVal == 101:
            return -1
        return returnVal

            
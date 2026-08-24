from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pSet, aSet=set(), set()
        pq,aq = deque(),deque()
        for x in range(len(heights)):
            for y in range(len(heights[0])):
                if x == 0 or y == 0:
                    pq.append((x,y))
                    pSet.add((x,y))
                if x == len(heights)-1 or y == len(heights[0])-1:
                    aq.append((x,y))
                    aSet.add((x,y))
        def bfs(q):
            temp = q
            visit=set()
            direc = [[0,-1],[0,1],[1,0],[-1,0]]
            while temp:
                curr = temp.popleft()
                for x,y in direc:
                    if curr[0] + x < 0 or curr[1] + y < 0 or curr[0] + x == len(heights) or curr[1] + y == len(heights[0]) or (curr[0]+x,curr[1]+y) in visit or heights[curr[0]+x][curr[1]+y] < heights[curr[0]][curr[1]]:
                            continue
                    temp.append((curr[0]+x,curr[1]+y))
                    visit.add((curr[0]+x,curr[1]+y))
            return visit
        p = bfs(pq)
        pSet = pSet.union(p)
        a = bfs(aq)
        aSet = aSet.union(a)
        return list(pSet.intersection(aSet))
                    

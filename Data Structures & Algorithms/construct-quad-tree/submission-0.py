"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        self.grid=grid
        def help(lowY, highY, lowX, highX):
            val = self.grid[lowY][lowX]
            if highX - lowX == 1 and highY - lowY == 1:
                return Node(val, True, None, None, None)
            for x in range(lowY, highY):
                for y in range(lowX, highX):
                    if self.grid[x][y] != val:
                        N = Node(False, False, None, None, None, None)
                        midY = lowY + (highY - lowY) // 2
                        midX = lowX + (highX - lowX) // 2
                        N.topLeft = help(lowY, midY, lowX, midX)
                        N.topRight = help(lowY, midY, midX, highX)
                        N.bottomLeft = help(midY, highY, lowX, midX)
                        N.bottomRight = help(midY, highY, midX, highX)
                        return N
            return Node(val, True, None, None, None, None)
        return help(0, len(grid), 0, len(grid[0]))
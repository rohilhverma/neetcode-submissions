class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = sorted(position)
        dct={}
        for x in range(len(position)):
            dct[position[x]] = (target - position[x]) / speed[x]
        numOfFleets = 0
        while stack:
            currentTopTime = dct[stack.pop()]
            numOfFleets += 1
            while stack and dct[stack[-1]] <= currentTopTime:
                stack.pop()
        
        return numOfFleets
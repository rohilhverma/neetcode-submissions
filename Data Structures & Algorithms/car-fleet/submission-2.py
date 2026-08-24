class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dct={}
        for x in range(len(position)):
            dct[position[x]] = (target - position[x]) / speed[x]       #time to get to finish line
        position.sort()
        fleet=0
        while position:
            fleet+=1
            curr=dct[position.pop()]
            while position and dct[position[-1]] <= curr:
                position.pop()
        return fleet
        

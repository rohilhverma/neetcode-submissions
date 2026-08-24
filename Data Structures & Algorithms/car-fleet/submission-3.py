class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dct={}
        for x in range(len(position)):
            dct[position[x]] = (target-position[x])/speed[x]
        position.sort()
        fleet=0
        
        while position:
            curr=dct[position.pop()]
            fleet+=1
            while position and curr >= dct[position[-1]]:
                position.pop()
        return fleet
            
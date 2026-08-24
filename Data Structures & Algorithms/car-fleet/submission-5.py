class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        lst=[]
        dct={}
        for x in range(len(position)):
            dct[position[x]] = speed[x]
        for x in sorted(position):
            lst.append((target-x)/dct[x])
        if lst:
            curr=lst.pop()
        fleet=1
        while lst:
            while lst and lst[-1] <= curr:
                lst.pop()
            if lst: 
                curr=lst.pop()
                fleet += 1
        return fleet
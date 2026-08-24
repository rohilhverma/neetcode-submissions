import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst=[]
        dct=defaultdict(list)
        for x in points:
            val = (x[0] ** 2 + x[1] ** 2) ** 0.5
            dct[val].append(x)
            heapq.heappush(lst, val)
        returnlst=[]
        while len(returnlst) < k:
            val = heapq.heappop(lst)
            coords = dct[val]
            while coords and len(returnlst) <k:
                returnlst.append(coords.pop())


        return returnlst
        



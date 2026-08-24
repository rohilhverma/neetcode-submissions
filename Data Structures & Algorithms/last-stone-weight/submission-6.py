import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            rocks= [heapq.heappop(heap),heapq.heappop(heap)]
            if rocks[0] > rocks[1]:
                x = rocks[1] + rocks[0]*-1
                
                heapq.heappush(heap, x)
            elif rocks[0] < rocks[1]:
                x = rocks[0] + rocks[1]*-1
                
                heapq.heappush(heap, x)
            else:
                continue

        return -1 * heapq.heappop(heap) if len(heap) else 0
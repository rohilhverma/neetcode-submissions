import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.lst=nums
        heapq.heapify(self.lst)
        self.k=k
        for x in range(len(nums) - k):
            heapq.heappop(self.lst)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.lst, val)
        for x in range(len(self.lst)-self.k):
            heapq.heappop(self.lst)
        return self.lst[0]

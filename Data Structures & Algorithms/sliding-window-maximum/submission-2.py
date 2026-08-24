from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        y=0
        lst=[]
        for x in range(len(nums)):
            if not q:
                q.append((nums[x],x))
            else:
                while q and q[-1][0] < nums[x]:
                    q.pop()
                q.append((nums[x],x))
            if x-y+1 == k:
                lst.append(q[0][0])
                if q[0][1]==y:
                    q.popleft()
                y+=1
        return lst



        
        
            


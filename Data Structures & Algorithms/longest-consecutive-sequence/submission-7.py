class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set(nums)
        streak=1
        if (len(nums)==0):return 0
        for x in nums:
            if x-1 in hashset:
                y=2
                while x+1 in hashset:
                    x+=1
                    y+=1
                streak=max(streak,y)
            else:
                hashset.add(x)
        return streak
        



            
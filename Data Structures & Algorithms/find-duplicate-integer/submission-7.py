class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lst=[0]*len(nums)

        for x in nums:
            if lst[x] == 0:
                lst[x]-=1
            else:
                return x
            
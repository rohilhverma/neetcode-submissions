class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lst=[0,0,0]
        for x in nums:
            lst[x] += 1
        
        i=0
        for x in range(len(nums)):
            if lst[i] == 0:
                while lst[i] == 0:
                    i+=1
            nums[x] = i
            lst[i]-=1
        
        return nums[x]

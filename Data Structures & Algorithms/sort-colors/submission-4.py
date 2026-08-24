class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors=[0,0,0]
        for x in nums:
            colors[x]+=1
       
        x=0
        y=0
        while x<len(nums):
            while y <= 2 and colors[y]==0 :
                y+=1
            nums[x] = y 
            x+=1
            colors[y]-=1


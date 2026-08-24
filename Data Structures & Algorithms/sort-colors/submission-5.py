class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors=[0,0,0]
        for x in nums:
            colors[x]+=1
        x=0
        for y in range(len(nums)):
            if colors[x] > 0:
                nums[y]=x
                colors[x]-=1
            else:
                while colors[x] <= 0:
                    x+=1
                nums[y]=x
                colors[x]-=1
        

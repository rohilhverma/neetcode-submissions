class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        y = 0
        while (y < len(nums)):
            if (nums[y] <= nums[x]):
                y+=1
                continue
            x+=1
            nums[x] = nums[y]
            y = x
        return x+1
            
        
        
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        end = len(nums)
        x=0
        while x < end:
            if nums[x] == val:
                end -= 1
                nums[x] = nums[end]
            else:
                x+=1
        return end
        


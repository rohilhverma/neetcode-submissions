class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        l,r = 0,len(nums)-1
        while l <= r:
            if nums[l] == val:
                while nums[r]==val and l<r:
                    r-=1
                if(l==r):return l
                nums[l],nums[r]=nums[r],nums[l]
                r-=1
            l+=1
        return l
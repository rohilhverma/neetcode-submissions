class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l,r=0,len(nums)-1
        lst=[]
        for x in range(len(nums)):
            l,r=x+1,len(nums)-1
            if x>0 and nums[x]==nums[x-1]:
                continue
            while l < r:
                if nums[l]+nums[r]+nums[x]>0:
                    r-=1
                    
                elif nums[l]+nums[r]+nums[x]<0:
                    l+=1
                    
                else:
                    lst.append([nums[l], nums[r],nums[x]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    l+=1
                    r-=1
            
            
                    
        return lst
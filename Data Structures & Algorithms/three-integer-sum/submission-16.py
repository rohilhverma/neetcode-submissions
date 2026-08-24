class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst=[]
        for x in range(len(nums)-2):
            if x >0 and nums[x] == nums[x-1]:
                continue
            l,r=x+1,len(nums)-1
            while l<r:
                if nums[l]+nums[r]+nums[x]==0:
                    lst.append([nums[l],nums[r],nums[x]])
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                elif nums[l]+nums[r]+nums[x]>0:
                    r-=1
                else:
                    l+=1
        return lst
        

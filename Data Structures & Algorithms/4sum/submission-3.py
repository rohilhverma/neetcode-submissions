class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        lst=[]
        nums.sort()

        for x in range(len(nums)):
            if x>0 and nums[x]==nums[x-1]:
                continue
            for y in range(len(nums)-1,-1,-1):
                if y<len(nums)-1 and nums[y]==nums[y+1]:
                    continue
                a,b=x+1,y-1
                while a<b:
                    if a > x+1 and nums[a] == nums[a-1]:
                        a+=1
                    elif b < y-1 and nums[b] == nums[b+1]:
                        b-=1
                    elif nums[a]+nums[b]+nums[x]+nums[y]==target:
                        lst.append([nums[a],nums[b],nums[x],nums[y]])
                        a+=1
                    elif nums[a]+nums[b]+nums[x]+nums[y]>target:
                        b-=1
                    elif nums[a]+nums[b]+nums[x]+nums[y]<target:
                        a+=1                
                        
        return lst
                                                
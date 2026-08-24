class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        lst=[]
        nums.sort()
        for x in range(len(nums)):
            if x >0 and nums[x] == nums[x-1]:
                continue
            for y in range(len(nums)-1, -1, -1):
                if y > x and len(nums) - 1 > y and nums[y] == nums[y+1]:
                    continue
                a,b=x+1,y-1
                while a<b:
                    if(nums[a]+nums[b]+nums[x]+nums[y] < target):
                        a+=1
                    elif(nums[a]+nums[b]+nums[x]+nums[y]> target):
                        b-=1
                    else:
                        lst.append([nums[a], nums[b], nums[x], nums[y]])
                        a+=1
                        b-=1
                        while a < b and nums[a] == nums[a-1]:
                            a+=1
            
        return lst
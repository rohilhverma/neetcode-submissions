class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst=[]
        nums.sort()
        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x-1]:
                continue
            y = x+1
            z = len(nums)-1
            while y < z:
                if nums[y]+nums[x]+nums[z] > 0:
                    z -= 1
                elif nums[y]+nums[x]+nums[z] <0:
                    y+=1
                else:
                    lst.append([nums[x], nums[y], nums[z]])
                    y+=1
                    z-=1
                    while y < z and nums[y] == nums[y-1]:
                        y+=1
        return lst

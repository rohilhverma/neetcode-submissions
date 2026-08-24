class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l, r = 0, len(nums)-1
        lst=[]
        while l < len(nums)-2:
            while l and l < len(nums)-2 and nums[l] == nums[l-1]:
                l+=1
            x, y = l+1, r
            while x < y:
                if nums[l] + nums[x]+nums[y] == 0:
                    lst.append([nums[l], nums[x], nums[y]])
                    x+=1
                    y-=1
                    while x < len(nums)-2 and nums[x] == nums[x-1]:
                        x+=1
                elif nums[l] + nums[x]+nums[y] > 0:
                    y-=1
                else:
                    x+=1
            l+=1
        return lst
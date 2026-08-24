class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst=[]
        for x in range(len(nums)-1):
            if x > 0 and nums[x-1] == nums[x]:
                continue
            else:
                y, z = x+1, len(nums)-1
                while y < z:
                    if nums[x] + nums[y] + nums[z] == 0:
                        lst.append([nums[x], nums[y], nums[z]])
                        y+=1
                        z-=1
                        while z > y and nums[y-1] == nums[y]:
                            y += 1
                    elif nums[x] + nums[y] + nums[z] > 0:
                        z -=1
                    else:
                        y += 1
        return lst
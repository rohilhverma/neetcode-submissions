class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst=[]

        temp=1
        for x in range(len(nums)):
            lst.append(temp)
            temp *= nums[x]
        temp=1
        for x in range(len(nums)-1, -1, -1):
            lst[x] *= temp
            temp *= nums[x]
    
        return lst
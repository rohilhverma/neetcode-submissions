class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        lst=[]
        prefix=1

        for x in nums:
            lst.append(prefix)
            prefix *= x
        postfix=1
        for x in range(len(nums)-1, -1, -1):
            lst[x] *= postfix
            postfix *= nums[x]
        return lst

        
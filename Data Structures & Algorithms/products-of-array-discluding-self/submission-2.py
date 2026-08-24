class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=1
        output=[]
        for x in nums:
            output.append(pre)
            pre *= x
        post=1
        for x in range(len(nums)-1,-1,-1):
            output[x] *= post
            post *= nums[x]
        return output

        
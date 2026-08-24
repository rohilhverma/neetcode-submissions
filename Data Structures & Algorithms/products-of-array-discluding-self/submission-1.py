class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = nums.copy()
        prefix = 1
        for x in range(len(output)):
            temp = output[x]
            output[x] = prefix
            prefix *= temp # every val in output represents the product of num before it
        postfix = 1
        for x in range(len(output)-1, -1, -1):
            output[x] *= postfix
            postfix *= nums[x]
        return output
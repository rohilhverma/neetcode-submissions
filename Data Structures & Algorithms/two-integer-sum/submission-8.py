class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for indx in range(len(nums)):
            diff = target - nums[indx]
            if diff in dict:
                return [nums.index(diff), indx]
            else:
                dict[nums[indx]] =  nums[indx]
        
        
        
        
        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct = {}
        for x in range(len(nums)):
            dct[nums[x]] = dct.get(nums[x], 0)+1
            if dct[nums[x]] >= (len(nums)/2):
                dct['answer'] = nums[x]
        return dct['answer']
    
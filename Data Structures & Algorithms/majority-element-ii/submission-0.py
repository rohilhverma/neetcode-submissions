class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dct={}
        for x in range(len(nums)):
            dct[nums[x]] = dct.get(nums[x], 0) + 1
        lst = []
        print(dct)
        for key,values in dct.items():
            if values > len(nums)/3:
                lst.append(key)
        return lst
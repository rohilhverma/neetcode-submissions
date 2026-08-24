class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dct = {}
        for x in nums:
            if x in dct:
                return dct[x]
            else:
                dct[x] = True
        return False
        
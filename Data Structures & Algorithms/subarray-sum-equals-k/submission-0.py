class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct={0:1}
        prefix=0
        count = 0
        for x in nums:
            prefix += x
            if (prefix - k) in dct:
                count += dct[prefix-k]
            dct[prefix] = dct.get(prefix, 0) + 1
        return count
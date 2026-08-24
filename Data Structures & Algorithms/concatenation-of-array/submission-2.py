class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = list(nums)
        for x in nums:
            ans.append(x)
        return ans
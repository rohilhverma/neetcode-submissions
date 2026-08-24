class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        x=0
        ans=[]
        while len(ans) < 2*len(nums):
            ans.append(nums[x])
            x+=1
            if x >= len(nums): x=0
        return ans

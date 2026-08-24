class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        returnArr=[]
        for x in range(2*numsLength):
            returnArr.append(nums[x % numsLength])
        return returnArr

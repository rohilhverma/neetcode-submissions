class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        comb=[]
        subComb=[]
        i=0
        nums.sort()
        def help(i, comb, subComb,s):
            if s == target:
                comb.append(subComb.copy())
            elif s>target:
                return
            
            for x in range(i, len(nums)):
                subComb.append(nums[x])
                help(x,comb, subComb, sum(subComb))
                subComb.pop()
        help(i, comb, subComb,0)
        return comb
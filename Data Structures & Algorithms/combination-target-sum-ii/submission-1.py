class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        lst=[]
        sublst=[]
        candidates.sort()
        def help(lst, sublst, s, i):
            if s == target:
                lst.append(sublst.copy())
                return
            elif s > target:
                return
            
            for x in range(i, len(candidates)):
                if x > i and candidates[x]==candidates[x-1]:
                    continue
                sublst.append(candidates[x])
                help(lst, sublst, sum(sublst), x+1)
                sublst.pop()
        help(lst, sublst, 0, 0)
        return lst

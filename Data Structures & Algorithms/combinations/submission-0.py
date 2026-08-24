class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb=[]
        subComb=[]
        i=1
        def help(i, subComb, comb):
            if len(subComb) == k:
                comb.append(subComb.copy())
            elif len(subComb)>k:
                return
            
            for x in range(i, n+1):
                subComb.append(x)
                help(x+1, subComb, comb)
                subComb.pop()
        
        help(i, subComb, comb)
        return comb
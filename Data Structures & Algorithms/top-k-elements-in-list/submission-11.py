class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct={}
        for x in nums:
            dct[x]=dct.get(x,0)+1
        
        lst=[[] for _ in range(len(nums)+1)]

        for x, y in dct.items():
            lst[y].append(x)
    
        returnLst=[]

        for x in range(len(lst)-1,-1,-1):
            currFreq=lst[x]
            if len(currFreq) == 0:
                continue
            else:
                while currFreq:
                    if len(returnLst) == k:
                        return returnLst
                    returnLst.append(currFreq.pop())
            

        return returnLst
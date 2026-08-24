class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct={}
        for x in nums:
            dct[x]=dct.get(x,0)+1
        
        freq=[]
        for _ in range(len(nums)+1):
            freq.append([])

        for x,y in dct.items():
            freq[y].append(x)
        
        returnlst=[]
        for x in range(len(freq)-1,-1,-1):
            y=freq[x]
            while y:
                if (len(returnlst) < k):
                    returnlst.append(y.pop())
                else:
                    break
        return returnlst
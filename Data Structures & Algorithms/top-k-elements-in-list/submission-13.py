class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        freq=[[] for x in range(len(nums))]

        for x in nums:
            occ[x] = occ.get(x, 0)+1

        for x, y in occ.items():
            freq[y-1].append(x)
        returnLst=[]
        for x in range(len(nums)-1, -1, -1):
            if not k:
                break
            while freq[x] and k:
                returnLst.append(freq[x].pop())
                k-=1
        return returnLst

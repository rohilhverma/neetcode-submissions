class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = [[] for _ in range(len(nums)+ 1)]
        dct ={}
        for x in nums:
            dct[x] = dct.get(x, 0) + 1
        for x, y in dct.items():
            lst[y].append(x)
        returnLst=[]
        y = len(nums)-1
        while k:
            z = lst[y]
            while k and z:
                val = z.pop()
                returnLst.append(val)
                k -=1
            y -=1
        return returnLst

            
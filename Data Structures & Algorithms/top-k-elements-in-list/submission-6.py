class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = [[] for _ in range(len(nums) + 1)]
        dct={}
        for x in range(len(nums)):
            dct[nums[x]] = dct.get(nums[x],0) + 1
        
        for key, values in dct.items():
            lst[values].append(key)
        kElements = []
        x = len(lst) - 1
        for x in range(len(lst) -1, -1, -1):
            for y in lst[x]:
                kElements.append(y)
                k -=1
                if (k ==0):
                    return kElements
        return kElements


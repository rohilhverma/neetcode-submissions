class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for x in range(len(nums)+1)]
        topK = []
        dct={}
        for num in nums:
            dct[num] = dct.get(num, 0) + 1
        for key, value in dct.items():
            arr[value].append(key)
        for x in range(len(arr)-1, 0, -1):
            if arr[x] != []:
                for n in arr[x]:
                    topK.append(n)
                    k -= 1
                    if k == 0:
                        return topK




        
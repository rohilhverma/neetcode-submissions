class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst=[]
        for x in range(len(nums)):
            lst.append([])
        hashMap = {}
        for x in nums:
            hashMap[x] = hashMap.get(x, 0) + 1
            lst.append([])
        for key, value in hashMap.items():
            lst[value].append(key)
        lst = lst[::-1]
        x = 0
        y = 0
        lst2 = []
        print(lst)
        while k: 
            if lst[x] == []:
                x += 1
                continue
            else:
                while k and y < len(lst[x]):
                    lst2.append(lst[x][y])
                    y += 1
                    k -= 1
                x += 1
                y=0
                
        return lst2
        
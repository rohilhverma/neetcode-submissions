class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dct={}
        hashSet= set(nums)
        longest = 0
        for x in range(len(nums)):
            curr=0
            if nums[x] - 1 not in hashSet:
                z = nums[x]
                while True:
                    if z in hashSet:
                        curr +=1
                        z += 1
                    else:
                        break
            if (curr > longest):
                longest = curr
        return longest
            

            
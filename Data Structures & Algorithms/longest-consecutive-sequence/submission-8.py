class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set(nums)
        seq=1
        if not nums:
            return 0
        for x in nums:
            if x-1 not in hashset:
                curr=1
                val=x+1
                while val in hashset:
                    curr+=1
                    val+=1
                seq =max(curr, seq)
        return seq
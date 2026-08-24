class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        y=0
        count=0

        for x in nums:
            if count==0:
                y=x
                count+=1
            elif x != y:
                count-=1
            else:
                count+=1
        return y
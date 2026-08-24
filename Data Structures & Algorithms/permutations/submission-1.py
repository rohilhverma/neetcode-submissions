class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def help(indx,lst):
            if indx >= len(nums):
                return [[]]
            lst=help(indx+1,lst)
            returnLst=[]
            for x in lst:
                for y in range(len(x)+1):
                    temp=x.copy()
                    temp.insert(y,nums[indx])
                    returnLst.append(temp)
            return returnLst
        return help(0,[])
            

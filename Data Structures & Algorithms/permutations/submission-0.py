class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def help(index, lst):
            if index == len(nums):
                return [[]]
            tempLst=[]
            perms = help(index+1, lst)

            for x in perms: 
                for y in range(len(x)+1):
                    z = x.copy()
                    z.insert(y, nums[index])
                    tempLst.append(z)
            return tempLst
        return help(0,[])
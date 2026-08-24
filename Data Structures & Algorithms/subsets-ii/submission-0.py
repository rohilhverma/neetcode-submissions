class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr, subArr=[],[]
        i=0
        def help(i, arr, subArr):
            if i >= len(nums):
                arr.append(subArr.copy())
            else:
                subArr.append(nums[i])
                help(i+1, arr, subArr)
                subArr.pop()
                while i+1<len(nums) and nums[i]==nums[i+1]:
                    i+=1
                help(i+1, arr, subArr)
        help(i, arr, subArr)
        return arr
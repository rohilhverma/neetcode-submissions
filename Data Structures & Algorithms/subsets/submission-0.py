class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        arr, subArr = [],[]
        i =0
        def help(i, arr, subArr):
            if i >= len(nums):
                arr.append(subArr.copy())
            else:
                subArr.append(nums[i])
                help(i+1, arr, subArr)
                subArr.pop()
                help(i+1, arr, subArr)
        help(i, arr, subArr)
        return arr
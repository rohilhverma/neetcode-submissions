class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lst=[0,0,0]
        
        for x in nums:
            lst[x]+=1
        print(lst)

        x = 0 # tracker for lst


        for y in range(len(nums)):
            if lst[x] > 0:
                nums[y] = x
                lst[x]-=1
            else:
                while lst[x] == 0:
                    x+=1
                nums[y]=x
                lst[x]-=1
        
        return nums
            
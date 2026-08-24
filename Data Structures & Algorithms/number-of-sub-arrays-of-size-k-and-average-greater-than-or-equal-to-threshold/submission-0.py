class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum=0
        num=0
        l=0
        for x in range(len(arr)):
            
            if x - l + 1 > k:
                sum-=arr[l]
                l+=1
            
            sum+=arr[x]
            
            if sum/(x-l+1) >= threshold and x-l+1 == k:
                num+=1
            
        return num
            
        
            

            
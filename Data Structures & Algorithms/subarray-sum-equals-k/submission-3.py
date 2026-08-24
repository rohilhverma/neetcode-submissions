class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dct={}
        prefix=0
        s=0
        for x in nums:    
            dct[prefix] = dct.get(prefix,0)+1
            prefix+=x
            if prefix - k in dct:
                s+=dct[prefix-k]
        return s
        
        
            
            
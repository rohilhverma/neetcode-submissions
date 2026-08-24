class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a,b=None,None
        c1,c2=0,0

        for x in nums:
            if x == a:
                c1+=1
            elif x == b:
                c2+=1
            elif c1 == 0:
                a=x
                c1+=1
            elif c2==0:
                b=x
                c2+=1
            else:
                c1-=1
                c2-=1
        
        count1, count2=0,0
        for x in nums:
            if x == a:
                count1+=1
            elif x == b:
                count2+=1
        
        if (count1 > len(nums)//3): 
            if (count2 > len(nums)//3):
                return [a,b]
            else:
                return [a]
        if (count2> len(nums)//3):return [b]
        return []

      

            
        
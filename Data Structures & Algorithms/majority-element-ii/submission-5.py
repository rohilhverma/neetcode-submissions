class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        e1,e2,c1,c2=None,None,0,0

        for x in nums:
            if x == e1:
                c1+=1
            elif x==e2:
                c2+=1
            elif c1==0:
                e1=x
                c1+=1
            elif c2 == 0:
                e2=x
                c2+=1
            else:
                c1-=1
                c2-=1
            

        c1,c2=0,0
        for x in nums:
            if x == e1:
                c1+=1
            elif x==e2:
                c2+=1
        
        res = []
        if c1 > len(nums)/3: res.append(e1)
        if c2 > len(nums)/3: res.append(e2)
        return res
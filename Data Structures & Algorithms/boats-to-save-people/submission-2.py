class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l,r,c=0,len(people)-1,0

        while l<=r:
            if (r==l):c+=1;break
            if people[l]+people[r]>limit:
                c+=1
                r-=1
            else:
                l+=1
                r-=1
                c+=1
        return c
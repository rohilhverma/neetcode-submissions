class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        x,y,count=0, len(people)-1,0
        while x<=y:
            if x != y and people[x]+people[y]>limit:
                count+=1
                y-=1
            else:
                count+=1
                x+=1
                y-=1
        return count
                
                
                

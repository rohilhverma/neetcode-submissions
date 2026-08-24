class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        lst=[]

        for x in asteroids:
            if x < 0 and lst and lst[-1]>0:
                while lst and lst[-1]>0 and lst[-1] < x * -1: 
                    lst.pop()
                if (len(lst) == 0):
                    lst.append(x)
                elif (lst[-1] == x * -1):
                    lst.pop()
                elif (lst[-1]<0):
                    lst.append(x)    
            else:
                lst.append(x)
        return lst
    
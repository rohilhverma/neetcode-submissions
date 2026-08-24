class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        lst=[]
        for x in asteroids:
            if lst and lst[-1]>0 and x<0:
                while lst and lst[-1] > 0 and abs(lst[-1]) < abs(x):
                    lst.pop()
                if (len(lst) == 0): #case of empty list
                    lst.append(x)
                elif lst[-1] * -1 == x: #case of breaking even
                    lst.pop()
                elif lst[-1] < 0:
                    lst.append(x)
            else:
                lst.append(x)
        return lst
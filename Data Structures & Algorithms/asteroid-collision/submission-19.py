class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        lst=[]
        for x in asteroids:
            if x < 0:
                if len(lst) == 0 or lst[-1] < 0:
                    lst.append(x)
                    continue
                while lst and lst[-1] > 0 and lst[-1] < x * -1 :
                    lst.pop()
                if len(lst) == 0 or lst[-1] <0:
                    lst.append(x)
                elif lst[-1] == x*-1:
                    lst.pop()
            else:
                lst.append(x)
        return lst
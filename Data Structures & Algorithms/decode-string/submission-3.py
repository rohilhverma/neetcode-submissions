class Solution:
    def decodeString(self, s: str) -> str:
        lst=[]
        for x in s:
            if x == "]":
                z=""
                while lst and lst[-1] != "[":
                    z = lst[-1] + z
                    lst.pop()
                lst.pop()
                y=""
                while lst and lst[-1].isdigit():
                    y = lst.pop() + y
                z *= int(y)
                lst.append(z)
            else:
                lst.append(x)
        return "".join(lst)
                
                

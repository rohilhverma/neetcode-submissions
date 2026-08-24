class Solution:
    def decodeString(self, s: str) -> str:
        lst=[]
        for x in s:
            if x == "]":
                s=""
                val=""
                while lst and lst[-1] != "[":
                    s = lst.pop() + s
                lst.pop() # remove [
                while lst and lst[-1].isdigit():
                    val=lst.pop()+val
                lst.append(int(val) * s)
            else:
                lst.append(x)
        return "".join(lst)
                

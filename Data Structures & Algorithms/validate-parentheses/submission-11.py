class Solution:
    def isValid(self, s: str) -> bool:
        dct={"{":"}", "[":"]","(":")"}
        lst=[]
        for x in s:
            if x in dct:
                lst.append(x)
            else:
                if lst and dct[lst[-1]] != x:
                    return False
                else:
                    if len(lst) == 0:
                        return False
                    lst.pop()
        if lst:
            return False
        return True
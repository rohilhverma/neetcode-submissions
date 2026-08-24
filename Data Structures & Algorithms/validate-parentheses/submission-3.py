class Solution:
    def isValid(self, s: str) -> bool:
        lst=[]
        if (len(s) % 2 == 1):
            return False
        for x in s:
            if x == '(' or x == '{' or x == '[':
                lst.append(x)
            else:
                if len(lst) == 0:
                    return False
                z = lst.pop()
                if z == "(":
                    if x != ")":
                        return False
                if z == "[":
                    if x != "]":
                        return False
                if z == "{":
                    if x != "}":
                        return False
        if (len(lst)) == 0:
            return True
        return False
                

        
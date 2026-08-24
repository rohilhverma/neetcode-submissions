class Solution:
    def isValid(self, s: str) -> bool:
        lst=[]
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
                

        
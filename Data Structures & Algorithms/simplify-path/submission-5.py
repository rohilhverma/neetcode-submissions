class Solution:
    def simplifyPath(self, path: str) -> str:
        path=path.split("/")
        lst=[]
        for x in path:
            if x == "/" or x =="." or x=="":
                continue  
            elif x == "..":
                if (lst):
                    lst.pop()
            else:
                lst.append(x)
            print(lst)
        s="/"
        for x in lst:
            s+=x
            s+="/"
        if(len(lst)==0):return "/"
        return s[:-1]
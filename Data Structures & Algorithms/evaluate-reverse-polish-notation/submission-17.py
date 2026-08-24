class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst=[]
        for x in tokens:
            if x == "+":
                lst.append(lst.pop()+lst.pop())
            elif x == "-":
                lst.append(-1*lst.pop()+lst.pop())
            elif x == "*":
                lst.append(lst.pop() * lst.pop())
            elif x =="/":
                y=lst.pop()
                lst.append(int(lst.pop()/y))
            else:
                lst.append(int(x))
            print(lst)
        return lst[-1]
                
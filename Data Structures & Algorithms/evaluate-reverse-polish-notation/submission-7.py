class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst=[]
        first = 0
        second = 0
        for x in tokens:
            if x not in ['+', '-', '*', '/']:
                lst.append(int(x))
            else:
                first = lst.pop()
                second = lst.pop()
                if x == '+':
                    lst.append(first + second)
                elif x == "-":
                    lst.append(second - first)
                elif x == "*":
                    lst.append(first * second)
                elif x == "/":
                    lst.append(int(second/first))
            print(lst)
        return lst[0]

                

        
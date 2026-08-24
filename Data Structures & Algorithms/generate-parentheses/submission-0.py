class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr,lst=[],[]
        o, c = n, n

        def help(o, c, arr, lst):
            if len(lst) == n+n:
                arr.append("".join(lst.copy()))
            else:
                if o == 0:
                    lst.append(")")
                    help(o, c-1, arr, lst)
                    lst.pop()
                elif c == 0:
                    lst.append("(")
                    help(o-1, c, arr, lst)
                    lst.pop()
                else:
                    lst.append("(")
                    help(o-1,c, arr, lst)
                    lst.pop()
                    if o < c:
                        lst.append(")")
                        help(o, c-1, arr, lst)
                        lst.pop()
        help(o, c, arr, lst)
        return arr


                
                
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = defaultdict(list, {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        })

        indx=0
        if len(digits)==0:
            return []
        def help(indx, lst):
            if indx == len(digits):
                return [""]
            returnLst=[]
            l = help(indx+1,lst)
            lst=digit_map[digits[indx]]
            for char in lst:
                for strs in l:
                    returnLst.append(char + strs)
            return returnLst
        return help(0,[])
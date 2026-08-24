class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def help(s, tup, hashset):
            if len(s) > len(word) or tup in hashset:
                return False
            elif s + board[tup[0]][tup[1]] == word:
                return True
            up, down, left, right = tup[0]-1, tup[0]+1, tup[1]-1, tup[1]+1

            if up >= 0:
                hashset.add(tup)
                if help(s + board[tup[0]][tup[1]], (up, tup[1]), hashset):
                    return True
                hashset.remove(tup)
            if down < len(board):
                hashset.add(tup)
                if help(s + board[tup[0]][tup[1]], (down, tup[1]), hashset):
                    return True
                hashset.remove(tup)
            if left >= 0:
                hashset.add(tup)
                if help(s + board[tup[0]][tup[1]], (tup[0], left), hashset):
                    return True
                hashset.remove(tup)
            if right < len(board[0]):
                hashset.add(tup)
                if help(s + board[tup[0]][tup[1]], (tup[0], right), hashset):
                    return True
                hashset.remove(tup)
        
            return False
        hashset=set()
        for x in range(len(board)):
            for y in range(len(board[x])):
                if help("", (x, y), hashset):
                    return True
        return False
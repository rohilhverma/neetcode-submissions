class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = ""
        for x in range(len(word1)):
            if x == len(word2): 
                word3 += word1[x:]
                return word3
            else:
                word3 += word1[x]
                word3 += word2[x]
        word3 += word2[len(word1):]
        return word3
class Solution:

    # Both O(n) time
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # "4#neet4#code"
            res += str(len(s)) + "#" + s
        return res 

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            # find "#"
            j = i
            while s[j] != "#":
                j += 1
            size = int(s[i:j])
            res.append(s[j+1 : j + 1 + size])
            
            # next string or end
            i = j + 1 + size
                
        return res





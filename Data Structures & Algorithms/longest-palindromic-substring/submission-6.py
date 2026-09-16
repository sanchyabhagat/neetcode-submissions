class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""
        resLen = 0
        slen = len(s)

        if len(s) == 1:
            return s[0]
        
        # else we loop through odd and even length palindromes

        for i in range(slen):
            # odd palindromes
            l = r = i
            
            while(l>=0 and r < slen and s[l] == s[r]):
                if r - l + 1 > resLen:
                    res = s[l: r+1]
                    resLen = r - l + 1
                r += 1
                l -= 1
        
            # even palindromes
            l = i
            r = i+1
            
            while(l>=0 and r < slen and s[l] == s[r]):
                if r - l + 1 > resLen:
                    res = s[l: r+1]
                    resLen = r - l + 1
                r += 1
                l -= 1
        
        return res
                    
            
        
        
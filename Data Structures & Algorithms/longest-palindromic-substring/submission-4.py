class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0
        size = len(s)

        if size == 1:
            return s

        # go through every element and keep moving outwards left and right to find potential palindromes
        # handle odd and even length case differently

        for i in range(size):
            # odd length palindrome
            l = r = i
            while l >= 0 and  r <= size-1 and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                r += 1
                l -= 1
            
            # even
            l = i
            r = i + 1
            while l >= 0 and  r <= size-1 and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                r += 1
                l -= 1
        
        return res
             
        
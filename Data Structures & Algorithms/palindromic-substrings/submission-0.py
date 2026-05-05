class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        # this approach makes sure we start at the middle element of palindrome reducing complexity from O(n^3) --> O (n^2)
        for i in range(len(s)):
            # odd length palindrome O n^2
            l = r = i
            while l >= 0 and  r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # even length palindrome O n^2
            l = i
            r = i+1
            while l >= 0 and  r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        return res
        
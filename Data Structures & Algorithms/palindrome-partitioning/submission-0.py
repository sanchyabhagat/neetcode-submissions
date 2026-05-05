class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return

            # loop from i -> end of word to find more possible palindrome combinations
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1]) # j+1 to include jth element in substring
                    # check more substrings
                    dfs(j+1)
                    # reset part
                    part.pop()
                
                
        
        dfs(0)
        return res

            
        
    # check for palindrome
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l = l+1
            r = r-1
            
        return True


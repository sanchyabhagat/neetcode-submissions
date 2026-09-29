class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charSet to check for repeats
        # as soon as we get a repeat - move window up left side
        # while we loop on right side
        #

        l = 0
        charSet = set()
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])

            res = max(r - l + 1, res)
        
        return res
        
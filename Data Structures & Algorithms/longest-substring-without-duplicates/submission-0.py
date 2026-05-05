class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maintain a set of cur substring
        # if s[r] is already in it, keep popping from left of set till we find it
        # once no duplicates, calculate curMax length
        # run the loop till the end
        l = 0
        maxL = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])

            # compare curMax with curMax substring with no duplicates
            maxL = max(maxL, r - l + 1)
        
        return maxL

            


        
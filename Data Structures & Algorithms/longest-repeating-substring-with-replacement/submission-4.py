class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = 0
        res = 0

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1

            while ((r - l + 1) - max(counts.values()) > k):
                counts[s[l]] = counts.get(s[l]) - 1
                l = l + 1
            
            res = max(res, r - l + 1)
        
        return res
        
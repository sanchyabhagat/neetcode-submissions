class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # map to store cur frequences
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            # increement count for element r
            count[s[r]] = count.get(s[r], 0) + 1

            # shrink window till we hit valid case
            while((r - l + 1) - max(count.values()) > k):
                count[s[l]] -= 1
                l = l + 1
            
            # after above loop, we should have a valid length
            res = max (res, r - l + 1)
        
        return res

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp will start from the end
        # for size of 8 eg neetcode, dp[8] = True
        # This means if we can reach dp[8] we can form all words correctly
        dp = {len(s):True}

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    
                    if(dp.get(i+ len(w), False)):
                        dp[i] = True
                
        return dp.get(0, False)

        
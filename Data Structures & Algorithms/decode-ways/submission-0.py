class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        # Base case of default one
        dp[len(s)] = 1

        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                dp[i] = 0

            else:
                # This is a valid single digit
                dp[i] = dp[i+1] 
            
            # Check if we got a double digit:
            if i+1 < len(s) and int(s[i] + s[i+1]) in range(10,27):
                dp[i] += dp[i+2]
        
        return dp[0]
        
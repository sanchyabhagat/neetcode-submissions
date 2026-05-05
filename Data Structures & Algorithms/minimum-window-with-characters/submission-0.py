class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # algorithim
        # check if t is empty -> return empty
        # add t1Counts to a hashmap
        # "need" -> t1Count unique totals
        # "have" -> current window matches, i.e. count matches EXACTLY to t1Count 
        # for a given char
        # if valid case -> have == need, save left and right index + length 
        # ONLY IF new found length < curLength
        # after valid case, start moving left window till need=have (valid case)

        if t == "":
            return ""
        tCount = {}
        cur = {}
        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)
        
        have, need = 0, len(tCount)
        res, resLen = [-1, -1], float("infinity")

        # initial window
        l = 0
        for r in range(len(s)):
            c = s[r]

            # add count to window
            cur[c] = 1 + cur.get(c, 0)

            # count for this char match
            if c in tCount and cur[c] == tCount.get(c):
                have += 1
            
            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # remove left element
                cur[s[l]] -= 1

                removedL = s[l]
                # remove "have" if there were matches
                if removedL in tCount and cur[removedL] < tCount[removedL]:
                    have -= 1
                
                # increment l
                l += 1
        
        if resLen == float("infinity"):
            return ""
        
        l, r = res
        # substring - l to r 
        return s[l: r+1]
                


        
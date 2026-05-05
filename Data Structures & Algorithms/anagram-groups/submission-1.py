class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## O(m * n) times
        ## O(m) space
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a...z
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # tuple because list cant be keys -- dont ask me why -- python sucks
            res[tuple(count)].append(s)
        
        return list(res.values())
                
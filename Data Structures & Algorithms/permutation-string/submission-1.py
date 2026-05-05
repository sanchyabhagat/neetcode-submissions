class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = ord('a')
        if len(s1) > len(s2):
            return False
        
        counts1, counts2 = [0] * 26, [0] * 26

        
        # matches = array of 26 a -> z, 1 = match, 0 no match
        # all 26 matches = True case
        matches = 0

        # get counts till s1 length
        for i in range(len(s1)):    
            counts1[ord(s1[i]) - a] += 1
            counts2[ord(s2[i]) - a] += 1
        
        # get cur matches - one time only so we know current state
        for i in range(26):
            if counts1[i] == counts2[i]:
                matches += 1
        
        l = 0
        # start for loop -> from len(s1) (inclusive) -> len(s2)
        for i in range(len(s1), len(s2)):
            # true case - all letters matches in substrings
            if matches == 26:
                return True
            
            # add right side of window
            index = ord(s2[i]) - a
            counts2[index] += 1
            if counts1[index] == counts2[index]:
                matches += 1
            elif counts1[index] + 1 == counts2[index]:
                matches -= 1
            
            # remove left side of window
            index = ord(s2[l]) - a
            counts2[index] -= 1
            if counts1[index] == counts2[index]:
                matches += 1
            elif counts1[index] - 1 == counts2[index]:
                matches -= 1

            l += 1

        return matches == 26  
        
         
        
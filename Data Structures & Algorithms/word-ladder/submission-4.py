class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        #adj list -> default to empty list on new additions
        nei = collections.defaultdict(list)
        
        wordList.append(beginWord)

        #build neighbor list using "*" patterns
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        
        # begin BFS now
        res = 1
        # oth visit and queueu will start with beginWord
        visit = set([beginWord])
        q = collections.deque()
        q.append(beginWord)

        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res
                
                # else find and add neighbors to Queue
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]

                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)

            res += 1

        # if early exit
        return 0
        
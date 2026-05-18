class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.numList = []
        

    def insert(self, val: int) -> bool:
        res = val not in self.numMap

        if res:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return res
        

    def remove(self, val: int) -> bool:
        res = val in self.numMap

        if res:
            # get index
            indx = self.numMap[val]
            last_val = self.numList[-1]
            # move last index item to this item being deleted to fill the gap
            self.numList[indx] = last_val
            
            # add new index for last element since we moved it
            self.numMap[last_val] = indx

            # delete
            self.numList.pop()
            del self.numMap[val]
        
        return res
        

    def getRandom(self) -> int:
        return random.choice(self.numList)
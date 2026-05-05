class TimeMap:

    def __init__(self):
        # This will store name -> [[value, timestamp]] mappings
        self.store = {} 
        
    # set will always be sorted since new timestamp > currentTimestamps in map
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])    
        

    def get(self, key: str, timestamp: int) -> str:
        res = "" # default if key doesn't exist

        values = self.store.get(key, [])

        # binary search
        l,r = 0, len(values)-1

        while l <= r:
            m = (l + r) // 2
            # check if this is valid or not
            if (values[m][1] <= timestamp):
                # cur value is valid
                res = values[m][0]

                # but let's check if we can find a closer value
                l = m + 1
            else:
                # check right side, but this is not a valid res
                r = m - 1
        return res

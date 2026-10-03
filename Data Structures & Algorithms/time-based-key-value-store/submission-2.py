class TimeMap:

    def __init__(self):
        # key : [(timestamp, value)]
        self.hsh = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hsh[key].append((timestamp, value)) # can append because time is increasing
        

    def get(self, key: str, timestamp: int) -> str:
        # binary sort because values always sorted by time 
        values = self.hsh[key]
        if not values:
            return ""

        l,r = 0, len(values)-1
        while l <= r:
            mid = (l+r)//2
            time, value = values[mid]
            if time == timestamp:
                return value
            elif time < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        
        # we dont find exact match
        return "" if r < 0 else values[r][1]
        

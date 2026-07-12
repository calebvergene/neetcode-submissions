class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # tasks with higher freq should be processed first
        # use a min heap with tuple (cooldown, -freq)
        # -freq so that the higher freqs get processed first 
        
        # first find frequency of all tasks
        task_freq = {}
        for task in tasks:
            task_freq[task] = task_freq.get(task, 0) + 1

        # now construct the heap
        pq = []
        for key in task_freq:
            heapq.heappush(pq, [0, -task_freq[key]])
        
        # now continuously pop from heap until its empty
        time = 0
        while pq:
            time += 1
            current = heapq.heappop(pq)
            if current[0] <= time:
                current[0] = time + n + 1
                current[1] += 1
                if current[1] != 0:
                    heapq.heappush(pq, current)
            else:
                heapq.heappush(pq, current)
        return time

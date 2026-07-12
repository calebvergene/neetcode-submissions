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
        count = 0
        while pq:
            count += 1
            current = heapq.heappop(pq)
            # task still needs cooldown, so doesn't count
            if count - current[0] < n:
                heapq.heappush(pq, current)
            else:
                current[0] = count
                current[1] += 1
                if current[1] < 0:
                    heapq.heappush(pq, current)
        return count

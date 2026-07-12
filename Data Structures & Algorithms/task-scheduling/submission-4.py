import heapq
from typing import List

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
            # Find a task that can be executed now
            temp = []
            executed = False
            
            while pq and not executed:
                current = heapq.heappop(pq)
                if current[0] <= time:
                    current[0] = time + n + 1
                    current[1] += 1
                    if current[1] != 0:
                        heapq.heappush(pq, current)
                    executed = True
                else:
                    temp.append(current)
            
            # Push back tasks that couldn't be executed
            for task in temp:
                heapq.heappush(pq, task)
        
        return time
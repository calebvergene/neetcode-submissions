class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # [x, z, y, y, y, y]
        # [y, x, z, y, y, y] n=2

        # prioritize tasks with the most frequency. 
        # heap 
        # (can_process_time, -frequency, task)

        # example heap:  keep a time counter 
        # pop (0, -3, "A")
        # proccess -> (time + cooldown, -2, "A")
        # add task back to queue

        heap = []
        freqs = collections.defaultdict(int)

        # get the frequency of each task
        for task in tasks: 
            freqs[task] += 1
        # add the tasks to our heap, (can_process, -freq, task)
        for task in freqs:
            heapq.heappush(heap, [0, -freqs[task], task])

        # start our task scheduler loop
        cycle = 0 
        while heap:
            task = heapq.heappop(heap)
            # can process task
            if task[0] <= cycle:
                task[1] += 1
                # if a task freq == 0, dont add back to heap
                if task[1] < 0:
                    task[0] = cycle + n + 1
                    heapq.heappush(heap, task)
            # cannot process task
            else:
                heapq.heappush(heap, task)
            cycle += 1

        return cycle






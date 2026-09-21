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
        q = deque()
        freqs = collections.defaultdict(int)

        # get the frequency of each task
        for task in tasks: 
            freqs[task] += 1
        # add the tasks to our heap, (-freq, task)
        for task in freqs:
            heapq.heappush(heap, [-freqs[task], task])

        # start our task scheduler loop
        cycle = 0 
        while heap or q:
            cycle += 1
            if heap:
                task = heapq.heappop(heap)
                task[0] += 1
                # if a task freq == 0, dont add back to heap
                if task[0] < 0:
                    task.append(cycle + n)
                    q.append(task)
            # process cooldown queue
            if q and q[0][-1] <= cycle:
                task = q.popleft()
                heapq.heappush(heap, task[:2])
            elif q and not heap and q[0][-1] > cycle:
                task = q.popleft()
                cycle = task[2]
                heapq.heappush(heap, task[:2])

        return cycle

        # [freq, cooldown, task]






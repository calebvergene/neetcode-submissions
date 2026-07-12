class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # use bfs
        if target == "0000": return 0

        seen = set(deadends)
        q = collections.deque()
        q.append('0000')

        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                code = q.popleft()
                # 4 different slots, 2 directions
                for slot in range(4):
                    up = code[:slot] + str((int(code[slot])+1+10)%10) + code[slot+1:]
                    down = code[:slot] + str((int(code[slot])-1+10)%10) + code[slot+1:]
                    if up not in seen:
                        seen.add(up)
                        if up == target: return level
                        q.append(up)
                    elif down not in seen:
                        seen.add(down)
                        if down == target: return level
                        q.append(down)
        return -1

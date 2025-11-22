from collections import deque

class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)

        # Remove all pings older than t - 3000
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)

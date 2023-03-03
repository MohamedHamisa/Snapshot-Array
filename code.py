class SnapshotArray(object):
    def __init__(self, n):
        self.cache = [[[-1, 0]] for _ in range(n)]
        self.i = 0

    def set(self, index, val):
        self.cache[index].append([self.i, val])

    def snap(self):
        self.i += 1
        return self.i - 1

    @lru_cache(maxsize=None)
    def get(self, index, snap_id):
        i = bisect.bisect(self.cache[index], [snap_id + 1]) - 1
        return self.cache[index][i][1]    


'''
Because self.cache[index] stores a list of [snap_id, val]. For example, you have [[0, 0], [1, 2], [1, 3]] at index 0, and you want to find the value at snapshot 1, what you need is bisect(self.cache[0], [1 + 1]) - 1.
'''

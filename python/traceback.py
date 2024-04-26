def combine77(n, k):
    res = []
    path = []
    def traceback(start):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            traceback(i + 1)
            path.pop()
    traceback(1)
    return res

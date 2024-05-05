def combinationSum216(k, n):
    path = []
    result = []
    def traceback(start):
        if len(path) == k and sum(path) == n:
            result.append(path[:])
        for i in range(start, 10):
            if start > n:
                break
            path.append(i)
            traceback(i + 1)
            path.pop()
    traceback(1)
    return result


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

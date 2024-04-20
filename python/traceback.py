def combine77(n, k):
    res = []

    def traceback(start, comb):
        if len(comb) == k:
            res.append(comb[:])
            return
        for i in range(start, n + 1):
            comb.append(i)
            traceback(i + 1, comb)
            comb.pop()

    traceback(1, [])
    return res

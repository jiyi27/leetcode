def combinationSum40(candidates, target):
    def backtrack(start, remain, path):
        if remain == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > remain:
                break
            path.append(candidates[i])
            backtrack(i + 1, remain - candidates[i], path)
            path.pop()

    candidates.sort()
    result = []
    backtrack(0, target, [])
    return result


def combinationSum39(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    path = []
    result = []

    def backtracking(cur_index, total):
        if total == target:
            result.append(path[:])
            return

        for i in range(cur_index, len(candidates)):
            if total + candidates[i] > target:
                break
            total += candidates[i]
            path.append(candidates[i])
            backtracking(i, total)
            total -= candidates[i]
            path.pop()

    candidates.sort()
    backtracking(0, 0)
    return result


def letterCombinations17(digits):
    letter_combination = []
    result = []
    letter_map = [
        " ",
        " ",
        "abc",  # 2
        "def",  # 3
        "ghi",  # 4
        "jkl",  # 5
        "mno",  # 6
        "pqrs",  # 7
        "tuv",  # 8
        "wxyz"  # 9
    ]

    def backtracking(current_index):
        if current_index == len(digits):
            result.append(''.join(letter_combination))
            return

        digit = int(digits[current_index])
        for letter in letter_map[digit]:
            letter_combination.append(letter)
            backtracking(current_index + 1)
            letter_combination.pop()

    if len(digits) == 0:
        return result
    backtracking(0)
    return result


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

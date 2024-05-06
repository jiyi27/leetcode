def letterCombinations17(self, digits):
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
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]

        def backtracing(current_index):
            if current_index == len(digits):
                result.append(''.join(letter_combination))
                return

            digit = int(digits[current_index])
            for letter in letter_map[digit]:
                    letter_combination.append(letter)
                    backtracing(current_index + 1)
                    letter_combination.pop()
        if len(digits) == 0:
            return result
        backtracing(0)
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

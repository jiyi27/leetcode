def romanToInt(s):
    m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = m[s[len(s) - 1]]
    for i in reversed(range(len(s) - 1)):
        if s[i] == "I" and (s[i + 1] == "V" or s[i + 1] == "X"):
            res -= 1
        elif s[i] == "X" and (s[i + 1] == "L" or s[i + 1] == "C"):
            res -= 10
        elif s[i] == "C" and (s[i + 1] == "D" or s[i + 1] == "M"):
            res -= 100
        else:
            res += m[s[i]]
    return res


def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    if len(strs[0]) == 0:
        return ""

    res = strs[0][0]
    for s in strs:
        if len(s) == 0:
            return ""
        if s[0] != res[0]:
            return ""

    f = True
    index = 1
    while True:
        for s in strs:
            if len(s) <= index:
                return res
            f = s[index] == strs[0][index]
            if not f:
                return res
        res += strs[0][index]
        index += 1


def longestCommonPrefix2(strs):
    res = strs[0]
    for i in range(1, len(strs)):
        while strs[i].startswith(res) is False:
            res = res[:-1]
    return res
 
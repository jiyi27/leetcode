def isAnagram(s, t):
    if len(s) != len(t):
        return False
    record = [0] * 26
    for c in s:
        record[ord(c) - ord('a')] += 1
    for c in t:
        record[ord(c) - ord('a')] -= 1
    for i in range(26):
        if record[i] != 0:
            return False
    return True
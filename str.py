def strStr(haystack, needle):
    if needle == "": return 0

    lps = [0] * len(needle)
    prevLPS, i = 0, 1
    while i < len(needle):
        if needle[i] == needle[prevLPS]:
            lps[i] = prevLPS + 1
            prevLPS, i = prevLPS + 1, i + 1
        elif prevLPS == 0:
            lps[i], i = 0, i + 1
        else:
            prevLPS = lps[prevLPS - 1]

    i = j = 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i, j = i + 1, j + 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]
        if j == len(needle):
            return i - len(needle)

    return -1


def reverseWords(s_):
    list_str = s_.split()
    list_str = list_str[::-1]
    return ' '.join(list_str)


def reverseStr(s: str, k: int) -> str:
    """
    1. 使用range(start, end, step)来确定需要调换的初始位置
    2. 对于字符串s = 'abc'，如果使用s[0:999] ===> 'abc'。字符串末尾如果超过最大长度，则会返回至字符串最后一个值，这个特性可以避免一些边界条件的处理。
    3. 用切片整体替换，而不是一个个替换.
    """
    def reverse_substring(text):
        left, right = 0, len(text) - 1
        while left < right:
            text[left], text[right] = text[right], text[left]
            left += 1
            right -= 1
        return text

    res = list(s)

    for cur in range(0, len(s), 2 * k):
        res[cur: cur + k] = reverse_substring(res[cur: cur + k])

    return ''.join(res)


def reverseString(s):
    left = 0
    right = len(s) - 1
    while left < right:
        temp = s[left]
        s[left], s[right] = s[right], temp
        left, right = left + 1, right - 1
    return s

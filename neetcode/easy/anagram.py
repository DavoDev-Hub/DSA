def isAnagram(s, t):
    if len(s) != len(t):
        return False
    char_counterS = {}
    char_counterT = {}
    for i in range(len(s)):
        char_counterS[s[i]] = 1 + char_counterS.get(s[i], 0)
        char_counterT[t[i]] = 1 + char_counterT.get(t[i], 0)
    return char_counterS == char_counterT


print(isAnagram('car', 'rac'))

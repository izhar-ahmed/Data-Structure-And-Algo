def romanToInteger(s):
    val = 0
    di = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000     
        }
    prevChar = s[0]
    val += di[prevChar]
    if len(s) == 1:
        return val
    for i in range(1, len(s)):
        if di[prevChar] < di[s[i]]:
            val += di[s[i]] - di[prevChar] - di[prevChar]
        else:
            val += di[s[i]]
        prevChar = s[i]
    return val
        

print(romanToInteger("MCMXCIV"))

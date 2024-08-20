def longestCommonPrefix(strs):
    cp = strs[0]
    for i in range(1, len(strs)):
        word = strs[i]
        temp = ""
        if len(cp) > len(word):
            for j in range(len(word)):
                if cp[j] != word[j]:
                    if j == 0:
                        return ""
                    else:
                        break
                elif cp[j] == word[j]:
                    temp += word[j]
            cp = temp
        else:
            for j in range(len(cp)):
                if cp[j] != word[j]:
                    if j == 0:
                        return ""
                    else:
                        break
                elif cp[j] == word[j]:
                    temp += word[j]
            cp = temp
    return cp

print(longestCommonPrefix(["flower","flow","flight"]))
                
def longestCommonPrefix2(strs):
    i = 1
    j = 0
    cp = strs[0]
    res = ""
    temp = ""
    if len(strs) == 1:
        res = strs[0]
        return res
    while i < len(strs):
        if j == len(strs[i]):
            j = 0
            i += 1
            temp = ""
        elif cp == "":
            return ""
        elif cp[j] != strs[i][j]:
            if j == 0:
                return ""
            j = 0
            i += 1
            temp = ""
        elif cp[j] == strs[i][j]:
            temp += strs[i][j]
            res = temp
            j += 1
    cp = res
    return cp
        




# Case 1: ["flower","flow","flight"]
# Case 2: ["dog","racecar","car"]
# Case 3: ["a"]
# Case 4: ["","b"]
# Case 5: ["a", "a", "b"]

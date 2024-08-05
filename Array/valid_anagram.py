class Solution(object):
    def isAnagram(self, s, t):
        hash1 = {}
        hash2 = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] in hash1:
                    hash1[s[i]] += 1
                else:
                    hash1[s[i]] = 1

            for i in range(len(t)):
                if t[i] in hash2:
                    hash2[t[i]] += 1
                else:
                    hash2[t[i]] = 1
            for key in hash1:
                if key in hash2:
                    if hash1[key] != hash2[key]:
                        return False
                else:
                    return False
            return True

solution = Solution()
print(solution.isAnagram("rat", "car"))
            

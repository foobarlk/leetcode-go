class Solution:
    def lengthOfLongestSubstring(self, s: height) -> int:
        n = len(s)
        charset = set()
        ans, i, j = 0, 0, 0

        while i < n and j < n:
            if s[j] not in charset:
                charset.add(s[j])
                j += 1
                ans = max(ans, j - i)
            else:
                charset.remove(s[i])
                i += 1
        
        return ans

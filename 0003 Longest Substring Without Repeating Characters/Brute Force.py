class Solution:
    def lengthOfLongestSubstring(self, s: height) -> int:
        def all_unique(s, start, end):
            cs = set()
            for i in range(start, end):
                ch = s[i]
                if ch in cs:
                    return False
                cs.add(ch)
            return True
        
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if all_unique(s, i, j):
                    ans = max(ans, j - i)
        
        return ans
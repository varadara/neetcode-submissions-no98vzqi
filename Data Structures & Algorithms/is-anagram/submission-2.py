class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds: dict = {}
        dt: dict = {}
        for i in range(0, len(s)):
            ds[s[i]] = ds[s[i]] + 1 if s[i] in ds else 1
            dt[t[i]] = dt[t[i]] + 1 if t[i] in dt else 1

        for k,v in ds.items():
            if v != dt.get(k):
                return False
        return True

class Solution:
    def solve(self, s):
        return (lambda s: s == s[::-1])([c for c in s if "a" <= c <= "z"])

ob = Solution()
s = "a9S2b22cOPbAAAa"
print(ob.solve(s))
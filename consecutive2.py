class Solution:
    def solve(self, s):
        temp = ""
        new = []
        for i in list(s):
            if i == temp:
                temp = i
            else:
                temp = i
                new.append(temp)
        return ''.join(new)
        
ob = Solution()
s = "XYYXY"
print(ob.solve(s))

class Solution:
    def solve(self, s):

        l1 = list(s)
        p1 = 0
        p2 = 1
        new_list = []
        if len(s) < 1:
            return s
        else:
            while p1 < len(l1):
                try:
                    if l1[p1] == l1[p2]:
                        p1 +=1; p2 += 1
                    else:
                        new_list.append(l1[p1])
                        p1 +=1; p2 += 1
                except IndexError:
                    new_list.append(l1[p1])
                    return ''.join(new_list)
                
        
ob = Solution()
s = ""
print(ob.solve(s))
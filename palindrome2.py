class Solution:
    def solve_lower_(self, s):
        return [c for c in s if "a" <= c <= "z"]
    def solve(self, s):
        if ''.join((self.solve_lower_(s))) == ''.join(reversed(self.solve_lower_(s))):
            return True
        else:
            print(self.solve_lower_(s))
            return False

    

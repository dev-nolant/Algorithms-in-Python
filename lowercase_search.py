def solve_upper_(s):
    return [c for c in s if "A" <= c <= "Z"]
def solve_lower_(s):
    return [c for c in s if "a" <= c <= "z"]
ls = "abcDDD"
# print(solve_upper_(ls))
print(solve_lower_(ls))
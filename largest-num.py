# passed in list = [5, 21, 2]
# program sorts list by number ([2, 5, 21])
# multiplies the second highest number by 2 and compares it to the largest ([5*2] <=> 21)
# if >, return False. if <, return True.

class Solution():
    def solve(self, n):
        self.sorted = []
        self.n = n
        def sort():
            size = len(self.n)
            output = [0] * size

            count = [0] * 10

            for m in range(0, size):
                count[self.n[m]] += 1

            for m in range(1, 10):
                count[m] += count[m - 1]

            m = size - 1
            while m >= 0:
                output[count[self.n[m]] - 1] = n[m]
                count[self.n[m]] -= 1
                m -= 1

            for m in range(0, size):
                self.n[m] = output[m]
            
            self.sorted = self.n
        
        def mathiply():
            new_apple = [
                (self.sorted[-2])*2
            ]
            return new_apple[0]
        sort()
        if mathiply() < self.sorted[-1]:
            return True
        else:
            return False
c = Solution()
nums = [3, 6, 15]
print(c.solve(nums))

class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))
        print(x)
        if(int(x[-1]) == 0):
            print("l")
            x = x[:-1]

        if(str(x[0]) == '-'):
            x = int(str(x)[1:-1])
            return x
        return 0

test = Solution()
print(test.reverse(1230))
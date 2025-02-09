def digits(n):
    return [int(x) for x in list(str(n))]

def square(x):
    return x ** 2

class Solution:
    def isHappy(self, n: int) -> bool:
        def go(n, acc):
            if n == 1:
                return True
            elif n in acc:
                return False
            else:
                acc.add(n)
                return go(sum(map(square, digits(n))), acc)

        return go(n, set())

    
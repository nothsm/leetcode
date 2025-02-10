def char_to_int(x):
    match x:
        case '0': return 0
        case '1': return 1
        case '2': return 2
        case '3': return 3
        case '4': return 4
        case '5': return 5
        case '6': return 6
        case '7': return 7
        case '8': return 8
        case '9': return 9
        case _: assert False

# little endian
def make_int(xs):
    def go(xs, b, acc):
        match xs:
            case []:
                return acc
            case [x, *xs]:
                return go(xs, b * 10, b * x + acc)
    return go(xs, 1, 0)

def string_to_int(s):
    def go(xs, acc):
        match xs:
            case []:
                return make_int(acc)
            case [x, *xs]:
                acc.append(char_to_int(x))
                return go(xs, acc)
    return go(list(reversed(s)), [])


class Solution:
    def multiply(self, x: str, y: str) -> str:
        return str(string_to_int(x) * string_to_int(y))
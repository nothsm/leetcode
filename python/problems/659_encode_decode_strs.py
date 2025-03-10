def encode(ss):
    return "".join([f"{len(s)}#" + s for s in ss])


def decode(s):
    i = 0
    ss = []
    while i < len(s):
        if s[i].isdigit():
            j = i
            while i < len(s) and s[i].isdigit():
                i += 1
            n = int(s[j:i])

            assert s[i] == "#"
            i += 1

            ss.append(s[i:i+n])
            i += n

            assert i == len(s) or s[i].isdigit()
    return ss



class Solution:

    def encode(self, strs: List[str]) -> str:
        return encode(strs)

    def decode(self, s: str) -> List[str]:
        return decode(s)

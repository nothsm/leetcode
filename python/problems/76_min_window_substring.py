from functools import partial

def bag(s):
    m = {}
    for c in s:
        m[c] = m.get(c, 0) + 1
    return m

def inbag(b1, b2):
    for c in b1:
        if b2.get(c, 0) < b1[c]:
            return False
    return True

def canCut(c, acc, target):
    return c not in target or acc[c] - 1 >= target[c]

def minWindow(s, t):
    bagt = bag(t)

    w = {}
    l = 0
    r = 0

    minl = 0
    minr = 0
    minlen = len(s) + 1

    have = 0
    need = len(bagt.keys())

    while l <= r:
        if have < need and r < len(s):
            if s[r] in bagt:
                w[s[r]] = w.get(s[r], 0) + 1
                # print(s[r], w[s[r]], bagt[s[r]])
                if w[s[r]] == bagt[s[r]]:
                    have += 1
            r += 1
        elif have >= need:
            if r - l < minlen:
                minlen = r - l
                minl = l
                minr = r

            if s[l] in bagt:
                w[s[l]] -= 1
                if w[s[l]] < bagt[s[l]]:
                    have -= 1
            l += 1
        else:
            return s[minl:minr]
    
        # print(w, l, r, have, need)

        # print(l, r, w, have, need)

    return s[minl:minr]

print(minWindow("ADOBECODEBANC", "ABC"))
print(minWindow("a", "a"))
print(minWindow("a", "aa"))

print(minWindow('bbaa', 'aba')) # should be 'baa'
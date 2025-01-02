import random

def randlist(n):
    return [random.randint(0, 10) for _ in range(n)]

def largestRectangleArea(hs):
    h_max = -1
    incs = []
    for r, hr in enumerate(hs):
        print(hr, incs, h_max)
        if incs:
            # l = r
            t, ht = incs[-1]
            while incs and incs[-1][1] > hr:
                l, hl = incs.pop()
                r = l

                h_max = max(h_max, (t - l + 1) * min(hl, ht))
            h_max = max(ht, h_max)

        incs.append((r, hr))

    print(incs)

    if incs:
        t, ht = incs[-1]
        while incs and incs[-1][1] >= hr:
            l, hl = incs.pop()
            h_max = max(h_max, (t - l + 1) * min(hl, ht))
        h_max = max(ht, h_max)

    return h_max


# only keep increasing values?
# check yourself on each index
# only need to check incs?

# [] how do you check on the last element?
# [] can I just pop everything after I check it?]
# [] greater than the min element in the queue?

# oldtop, maybe dont need smaller elements

# smallest element to the left of the last element

# [(0, 2), (1, 1), (2, 5), (3, 6)]
# [(0, 2), (2, 5), (3, 6)]
# [(0, 2), (2, 5), (3, 6)]


# monotonically increasing list

# print(largestRectangleArea(randlist(5)))

print(largestRectangleArea([2, 1, 5, 6, 2, 3])) # 10
print(largestRectangleArea([2, 4])) # 4
# print(largestRectangleArea([2, 1, 3]))

print(largestRectangleArea([1, 7, 7, 8, 7])) # 28
# print(largestRectangleArea([10, 0, 3, 8, 5, 4])) # 12 TODO
# print(largestRectangleArea([2, 10, 8])) # 16
# print(largestRectangleArea([0, 2])) # 2
# print(largestRectangleArea([1, 9, 4, 0])) # 9
# print(largestRectangleArea([1, 10, 7, 6, 6])) # 24
# print(largestRectangleArea([1, 8, 7, 6, 8, 9, 3, 5, 1, 7])) # 30
# print(largestRectangleArea([2, 4, 3, 8, 10, 1, 10, 0, 3, 1])) # 16
# print(largestRectangleArea([9, 6, 0, 7, 8])) # TODO
# print(largestRectangleArea([10, 1, 7, 7, 10])) # TODO
# print(largestRectangleArea([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3])) # 14
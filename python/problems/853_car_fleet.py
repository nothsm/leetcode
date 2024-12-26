def carFleet(target, position, speed):
    # print(list(zip(position, speed)))
    ps = iter(sorted(zip(position, speed), key=lambda xy: xy[0], reverse=True))
    # print(ps)
    pos1, speed1 = next(ps)
    ts = [(target - pos1) / speed1]
    for pos, speed in ps:
        t = (target - pos) / speed
        if t > ts[-1]:
            ts.append(t)
    
    return len(ts)


print(carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))

print(carFleet(10, [3], [3]))

print(carFleet(100, [0, 2, 4], [4, 2, 1]))
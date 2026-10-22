def solution(dirs):
    answer = 0
    dx = 0
    dy = 0
    roads = set()

    for d in dirs:
        next_dx = dx
        next_dy = dy

        if d == "U":
            next_dy -= 1
        elif d == "D":
            next_dy += 1
        elif d == "R":
            next_dx += 1
        elif d == "L":
            next_dx -= 1

        if not (-5 <= next_dx <= 5 and -5 <= next_dy <= 5):
            continue

        before = (dx, dy)
        after = (next_dx, next_dy)
        road = tuple(sorted([before, after]))

        if road not in roads:
            roads.add(road)
            answer += 1

        dx = next_dx
        dy = next_dy

    return answer
def solution(n):
    ans = n
    battery = 0

    while ans != 0:
        if ans % 2 == 0:
            ans = ans // 2
        else:
            ans -= 1
            battery += 1

    return battery
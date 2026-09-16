def solution(park, routes):
    answer = []

    #스타트 파악
    for i in park:
        if "S" in i:
            start = [park.index(i), i.index("S")]
            break

    #이동
    ro = start[1]
    co = start[0]
    for r in routes:
        op, n_str = r.split()
        n = int(n_str)

        if op == "E":
            if (ro + n) >= len(park[0]):
                pass
            else:
                for j in range(n):
                    ro += 1
                    if park[co][ro] == "X":
                        ro -= (j + 1)
                        break
        elif op == "W":
            if (ro - n) < 0:
                pass
            else:
                for j in range(n):
                    ro -= 1
                    if park[co][ro] == "X":
                        ro += (j + 1)
                        break
        elif op == "N":
            if (co - n) < 0:
                pass
            else:
                for j in range(n):
                    co -= 1
                    if park[co][ro] == "X":
                        co += (j + 1)
                        break
        elif op == "S":
            if (co + n) >= len(park):
                pass
            else:
                for j in range(n):
                    co += 1
                    if park[co][ro] == "X":
                        co -= (j + 1)
                        break


    answer.append(co)
    answer.append(ro)

    return answer
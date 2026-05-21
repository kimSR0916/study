def solution(array, commands):
    answer = []

    for cmd in commands:
        i = cmd[0] - 1
        j = cmd[1]
        k = cmd[2] - 1

        tmp = array[i:j]
        tmp.sort()

        answer.append(tmp[k])

    return answer
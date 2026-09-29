import heapq


def solution(k, score):
    answer = []
    tmp = []

    for i in score:
        if len(tmp) < k:
            heapq.heappush(tmp, i)
        elif tmp[0] < i:
            heapq.heappop(tmp)
            heapq.heappush(tmp, i)
        answer.append(tmp[0])

    return answer
def solution(strings, n):
    answer = strings

    answer.sort(key=lambda x: (x[n], x)) # 람다 x[n]의 값을 반환 즉 키는 x[n]의 값이
    return answer
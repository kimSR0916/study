def solution(arr1, arr2):
    answer = []

    for i in range (len(arr1)):
        row = []
        for j in range (len(arr1[i])):
            row.append(arr1[i][j] + arr2[i][j])
        answer.append(row)
        
    return answer

#2차풀이
def solution(arr1, arr2):
    answer = arr1

    for i in range (len(arr2)):
        for j in range (len(arr2[i])):
            answer[i][j] += arr2[i][j]
        
    return answer

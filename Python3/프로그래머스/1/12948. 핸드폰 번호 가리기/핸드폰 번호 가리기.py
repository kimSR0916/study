def solution(phone_number):
    answer = ''
    
    num = phone_number[-4:]

    answer = ('*' * (len(phone_number) - 4) + num)
    return answer
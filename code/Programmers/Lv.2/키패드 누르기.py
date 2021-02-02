def solution(numbers, hand):
    result = ''
    answer = []
    length = len(numbers)
    for i in range(length):
        if numbers[i] == 0:
            numbers[i] = 11

    l = 10
    r = 12
    for i in range(length):
        n = numbers[i]
        if n % 3 == 1:
            answer.append('L')
            l = n
            continue
        if n % 3 == 0:
            answer.append('R')
            r = n
            continue

        ld = 0;
        rd = 0
        # 가운데 눌러야하는경우
        if l % 3 == 1:  # 왼쪽에있는경우
            ld = abs(n - (l + 1)) // 3 + 1  # 거리
        else:
            ld = abs(n - l) // 3
        if r % 3 == 0:  # 오른쪽에 있는경우
            rd = abs(n - (r - 1)) // 3 + 1
        else:
            rd = abs(n - r) // 3
        if ld == rd:
            if hand == 'right':
                r = n
                answer.append('R')
            else:
                l = n
                answer.append('L')
        if ld < rd:
            answer.append('L')
            l = n
        if rd < ld:
            answer.append('R')
            r = n
    result = ''.join(answer)
    return result

"""
문제
numbers : [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]   //눌러야하는 숫자 리스트
hand : "right" // 손잡이 
result : "LRLLLRLLRRL" //눌려지는 결과 result로 출력

https://programmers.co.kr/learn/courses/30/lessons/67256
"""

"""
문제 접근

단순한 구현 문제였고 가운데 누르는 경우만 조금 신경써서 구현해주면 됐다.
"""

"""
문제 풀이

n=numbers[i],  if n%3 == 1 //이와 같이 n%3으로 해당 위치를 구분하였다.

가운데 버튼을 눌러야하는경우
abs를 이용하여 각각 위치에서 눌러야하는 키의 거리를 쉽게 계산하였고 더해주었다.
"""

"""
문법
str() 하면 모든 타입을 str 타입으로 변경해주는것 , 리스트-> 문자열로 만들기 위해서는
"".join(리스트명) 으로 조합해주기

string더하기 시간복잡도
1. s+='R'  
O(N^2)  O(A)+O(B) 만큼 의 새로운 스트링을 만들기때문에 N^2
2. "".join(리스트명)
O(N)

결론: 스트링 더할때 리스트로 append하다가 마지막에 join으로 string만들어주는게 좋다.
"""
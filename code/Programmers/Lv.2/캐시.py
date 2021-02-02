from collections import deque


def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    answer = 0
    st = set()
    dq = deque()
    l = len(cities)
    for i in range(l):
        country = cities[i].upper()

        # cache에 있는 경우
        if country in st:
            dq.remove(country)
            dq.append(country)
            answer += 1
            continue

        # 없는 경우
        if len(dq) >= cacheSize:
            st.remove(dq.popleft())
        st.add(country)
        dq.append(country)
        answer += 5

    return answer

solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])
solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
             "Rome"])
solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])

"""
문제
LRU알고리즘 사용하는 캐시를 이용하여 
주어진 cacheSize대로 DB처리시 발생하는 비용 구하시오
cachemiss - 5
cachehit  - 1
"""

"""
문제 접근
매번 리스트를 순회하여 해당 키가 있는지 확인하는것은 비효율적이므로 dictionary를 이용하였고
오랜된 것은 빼내야하므로 list보단 deque을 이용하였다.
"""

"""
문제 풀이
set,deque사용

다른 풀이는
deque(maxlen=cachSize)를 이용해서 불필용한 연산(dic에 있는지 확인)을 제거했다.

"""


# Target: 검색 대상 // Pattern: 패턴

def bruteForce(pattern, target):
    N = len(target) # 검색 대상의 길이
    M = len(pattern) # 검색 패턴의 길이

    i = 0 # target의 인덱스
    j = 0 # pattern의 인덱스

    # 각 인덱스가 타겟과 패턴의 길이보다 작을동안 반복
    while j < M and i < N:
        # 패턴과 다른 곳을 발견했을 때
        if target[i] != pattern[j]:
            # j만큼 온 상태에서 틀린 곳을 발견함
            # 지금 위치 - j + 1 이 다음 위치가 된다.
            i = i - j
            # -1로 j를 초기화 하는 이유, 패턴과 일치하는 문자열이 발견 되었을 때
            # j + 1을 해주기 때문
            j = -1

        # 패턴과 같을 때
        i = i + 1
        j = j + 1

        if j == M:
            # 패턴 인덱스 j 가 M 까지 가게되면 탐색 된 것 == 탐색 성공
            return True
        else:
            return False
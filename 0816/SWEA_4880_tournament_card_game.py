T = int(input())

# 오른쪽이 이기는 경우를 win으로 둔다.
win = [(1, 2), (2, 3), (3, 1)]
def card_game(students, card_list):
    # 2명까지 남으면 승자를 뽑는다.
    if len(students) == 2:
        # student - 1이 card_list 의 인덱스
        if (card_list[students[0] - 1], card_list[students[1] - 1]) in win:
            return students[1]
        else:
            return students[0]
    # 한 명일 경우에는 그 사람이 그대로 승자
    elif len(students) == 1:
        return students[0]
    # 재귀함수로 계속 반으로 쪼개면서 i와 j를 만들고 마지막에 i와 j에 대해 함수 계산
    # 보기에 나온 것처럼 계산하고 N 은 인덱스이므로 1을 빼준 값을 넣는다.
    else:
        N = (len(students) + 1) // 2
        i = card_game(students[:N], card_list)
        j = card_game(students[N:], card_list)
        return card_game([i, j], card_list)

for case in range(1, T + 1):
    N = int(input())
    card_list = list(map(int, input().split()))
    students = list(range(1, N + 1))

    print(f'#{case} {card_game(students, card_list)}')
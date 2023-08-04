T = int(input())

for case in range(1, T + 1):
    D, A, B, F = map(int, input().split())

    # 파리가 날아가는 시간은 충돌할 때까지의 시간이므로 속력에서 시간을 곱하면 답
    fly = F * D / (A + B)
    print(f'#{case} {fly}')
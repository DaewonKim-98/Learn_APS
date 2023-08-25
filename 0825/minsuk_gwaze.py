T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())
    klist = list(map(int, input().split()))

    students = list(range(1, N + 1))
    for k in klist:
        students.remove(k)

    print(f'#{case}', end=' ')
    print(*students)
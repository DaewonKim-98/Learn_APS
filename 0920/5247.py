import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

cal = ['+ 1', '- 1', '* 2', '- 10']

def bfs(N):
    q = []
    visited = [0] * 1000001
    i = 0
    # 횟수를 셀 0과 계산할 N
    q.append(N)
    visited[N] = 1
    while len(q) >= 0:
        p = q[i]
        i += 1
        # print(q)
        # 계산이 끝났을 때 M이면 종료
        if p == M:
            print(f'#{case} {visited[p] - 1}')
            break
        for c in cal:
            if c == '+ 1':
                if p + 1 > 1000000:
                    continue
                else:
                    if visited[p + 1] == 0:
                        q.append(p + 1)
                        visited[p + 1] = visited[p] + 1
            elif c == '- 1':
                if p - 1 < 1:
                    continue
                else:
                    if visited[p - 1] == 0:
                        q.append(p - 1)
                        visited[p - 1] = visited[p] + 1
            elif c == '* 2':
                if p * 2 > 1000000:
                    continue
                else:
                    if visited[p * 2] == 0:
                        q.append(p * 2)
                        visited[p * 2] = visited[p] + 1
            else:
                if p - 10 < 1:
                    continue
                else:
                    if visited[p - 10] == 0:
                        q.append(p - 10)
                        visited[p - 10] = visited[p] + 1



T = int(input())
for case in range(1, T + 1):
    N, M = map(int, input().split())

    bfs(N)
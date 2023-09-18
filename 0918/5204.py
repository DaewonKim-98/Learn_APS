import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def merge(left, right):
    result = []
    i, j = 0, 0

    while len(left) > j or len(right) > i:
        # 둘 다 남아있으면
        if len(left) > j and len(right) > i:
            if left[j] >= right[i]:
                result.append(right[i])
                i += 1
            else:
                result.append(left[j])
                j += 1
        # 하나만 남아있으면
        elif len(left) > j:
            result.append(left[j])
            j += 1
        elif len(right) > i:
            result.append(right[i])
            i += 1

    return result

def merge_sort(arr):
    global cnt
    if len(arr) == 1:
        return arr
    n = len(arr)

    left = arr[:n // 2]
    right = arr[n // 2:]

    left = merge_sort(left)
    right = merge_sort(right)
    if left[-1] > right[-1]:
        cnt += 1
    return merge(left, right)

T = int(input())
for case in range(1, T + 1):
    cnt = 0
    N = int(input())
    arr = list(map(int, input().split()))
    arr = merge_sort(arr)
    print(f'#{case} {arr[N // 2]} {cnt}')


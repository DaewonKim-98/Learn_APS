import sys
sys.stdin = open('input.txt')

T = int(input())

def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for i in arr:
        if i < pivot:
            lesser_arr.append(i)
        elif i > pivot:
            greater_arr.append(i)
        else:
            equal_arr.append(i)
    return quick(lesser_arr) + equal_arr + quick(greater_arr)


for case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = quick(arr)[N // 2]
    print(f'#{case} {result}')

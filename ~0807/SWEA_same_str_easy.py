T = int(input())

for case in range(1, T + 1):
    arr = list(input().strip())

    read = True
    # 하나라도 거꾸로 읽어서 잘못된게 있으면 read = False
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr) - 1 - i]:
            read = False

    if read == True:
        print(f'#{case} {1}')
    else:
        print(f'#{case} {0}')
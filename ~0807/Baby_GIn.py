T = int(input())

for case in range(1, T + 1):
    arr = list(map(int, input()))
    # 오름차순으로 정렬
    for i in range(5, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # 오름차순으로 정렬된 것에 대해 앞 3개가 같을 때
    if (arr[0] == arr[1] == arr[2]) | (arr[0] + 2 == arr[1] + 1 == arr[2]):
        # 뒤에 3개가 같으면 1
        if arr[3] == arr[4] == arr[5]:
            result = 1
        # 뒤에 3개가 연속이면 1
        elif arr[3] + 2 == arr[4] + 1 == arr[5]:
            result = 1
        # 아니면 0
        else:
            result = 0
    # 2개씩 중복될 때
    elif arr[0] + 2 == arr[2] + 1 == arr[4]:
        result = 1
    # 모든 경우가 없으면 0
    else:
        result = 0

    print(f'#{case} {result}')





























# while True:
#     sentence = str(input())
#     if sentence == '.':
#         break
#
#     balance = True
#     for i in range(len(sentence)):
#         for j in range(i, len(sentence)):

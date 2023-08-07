T = int(input())

dic = {
    'ZRO': 0,
    'ONE': 1,
    'TWO': 2,
    'THR': 3,
    'FOR': 4,
    'FIV': 5,
    'SIX': 6,
    'SVN': 7,
    'EGT': 8,
    'NIN': 9,
}
for case in range(1, T + 1):
    A, B = map(str, input().split())
    arr = list(map(str, input().split()))

    # 문자열로 들어온 것들을 딕셔너리를 통해 숫자로 바꿔준다.
    new_arr = []
    for i in arr:
        new_arr += [dic[i]]

    # 숫자 리스트를 오름차순으로 정렬
    for j in range(int(B), 1, -1):
        for k in range(1, j):
            if new_arr[k - 1] > new_arr[k]:
                new_arr[k - 1], new_arr[k] = new_arr[k], new_arr[k - 1]

    print(f'#{case}')
    # 숫자를 다시 딕셔너리를 통해 문자열로 변경
    for l in new_arr:
        for k, v in dic.items():
            if v == l:
                print(k, end=' ')
    print()
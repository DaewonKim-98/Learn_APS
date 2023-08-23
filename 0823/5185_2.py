s = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
# 16진수의 인덱스를 딕셔너리 형태로 만든다.
dic = {}
for i in range(16):
    dic[s[i]] = i

T = int(input())

for case in range(1, T + 1):
    N, num = map(str, input().split())
    num_list = list(num)
    # 각각의 자리 수에 대해 2진수로 표현
    output = ''
    for n in num_list:
        for j in range(3, -1, -1):
            # 딕셔너리에서 16진수를 꺼내온다.
            if int(dic[n]) & (1 << j):
                output += '1'
            else:
                output += '0'
    print(f'#{case} {output}')
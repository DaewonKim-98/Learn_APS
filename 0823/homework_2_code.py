T = int(input())

# 코드 딕셔너리
code_dic = {}
code_dic['0001101'] = 0
code_dic['0011001'] = 1
code_dic['0010011'] = 2
code_dic['0111101'] = 3
code_dic['0100011'] = 4
code_dic['0110001'] = 5
code_dic['0101111'] = 6
code_dic['0111011'] = 7
code_dic['0110111'] = 8
code_dic['0001011'] = 9

for case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    a = 0
    b = 0
    for r in range(N):
        for c in range(M - 55):
            # 1이 나오고 가장 뒤가 1인 부분, 즉 암호인 부분을 찾는다.
            if arr[r][c + 3] == '1':
                if arr[r][c + 55] == '1' and '1' not in arr[r][c + 56:-1]:
                    a, b = r, c
                    break
            elif arr[r][c + 2] == '1':
                if arr[r][c + 55] == '1' and '1' not in arr[r][c + 56:-1]:
                    a, b = r, c
                    break
            elif arr[r][c + 1] == '1':
                if arr[r][c + 55] == '1':
                    a, b = r, c
                    break
    # 코드를 code_dic을 통해 만든다.
    code = []
    for i in range(0, 56, 7):
        code.append(code_dic[arr[a][b + i:b + i + 7]])

    # 암호 해독
    decoding = 0
    for i in range(4):
        # 홀수번째는 3 곱한걸 더하고 짝수는 그냥 더함 (인덱스라서 홀짝 반대로)
        decoding += code[i * 2] * 3
        decoding += code[i * 2 + 1]

    if decoding % 10 == 0:
        print(f'#{case} {sum(code)}')
    else:
        print(f'#{case} {0}')



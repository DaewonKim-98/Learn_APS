T = int(input())

for case in range(1, T + 1):
    binary = list(map(int, input()))
    strikeouts = list(map(int, input()))

    # 이진수에서 한 자리만 잘못되었으므로 각 자리를 고친 이진수 저장
    fixed_binary = []
    for i in range(len(binary)):
        # 각 자리를 고친 뒤 fixed_binary에 추가
        copy_binary = binary[:]
        if copy_binary[i] == 0:
            copy_binary[i] = 1
        else:
            copy_binary[i] = 0
        fixed_binary.append(copy_binary)

    # 삼진수에서 한 자리만 잘못되었으므로 각 자리를 고친 삼진수 저장
    fixed_strikeouts = []
    for i in range(len(strikeouts)):
        # 각 자리를 고친 뒤 fixed_strikeouts 에 추가
        for j in range(3):
            for k in range(3):
                copy_strikeouts = strikeouts[:]
                if j != k:
                    if copy_strikeouts[i] == j:
                        copy_strikeouts[i] = k
                        fixed_strikeouts.append(copy_strikeouts)

    # 만들 수 있는 십진수 리스트
    ten_list2 = []
    for b in fixed_binary:
        # 십진수로 만들기
        ten = 0
        # 이진수를 십진수로 저장
        # 뒤에서부터 0이므로
        for i in range(len(binary)-1, -1, -1):
            ten += 2 ** (len(binary)-1 - i) * b[i]
        ten_list2.append(ten)

    # 만들 수 있는 십진수 리스트
    ten_list3 = []
    for b in fixed_strikeouts:
        # 십진수로 만들기
        ten = 0
        # 이진수를 십진수로 저장
        # 뒤에서부터 0이므로
        for i in range(len(strikeouts)-1, -1, -1):
            ten += 3 ** (len(strikeouts)-1 - i) * b[i]
        ten_list3.append(ten)

    # 같은 것을 출력
    for i in ten_list2:
        for j in ten_list3:
            if i == j:
                print(f'#{case} {i}')
























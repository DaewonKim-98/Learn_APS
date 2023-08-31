T = int(input())

for case in range(1, T + 1):
    arr, N = list(map(int, input().split()))
    arr = list(str(arr))
    sorted_arr = sorted(arr, reverse=True)

    # 중복되는 것이 있는지 찾기
    duplicate = False
    for i in range(10):
        if arr.count(str(i)) > 1:
            duplicate = True
    # 교체 횟수가 N이 될 때까지 반복
    cnt = 0
    i = 0
    max_idx_list = []
    while cnt < N:
        # 내림차순으로 정렬이 완료 되었을 때
        if arr == sorted_arr:
            # 남은 카운트가 짝수이면 그대로 출력
            if (N - cnt) % 2 == 0:
                break
            # 남은 카운트가 홀수이면
            else:
                # 중복되는 수가 있으면
                if duplicate == True:
                    break
                # 중복되는 수가 없으면 가장 뒤에 있는 숫자들을 바꾸기
                else:
                    arr[-1], arr[-2] = arr[-2], arr[-1]
                    break

        # i 인덱스 이상일 때 최댓값이 항상 앞으로 오도록
        max_idx = i
        for j in range(i, len(arr)):
            if arr[max_idx] <= arr[j]:
                max_idx = j
        # i번째가 앞에서부터이므로 i번째를 maxidx랑 교체
        if i != max_idx:
            # 만약 최댓값이 여러개면 단순히 가장 뒤에 것을 바꾸어 주면 안되고
            # 인덱스들을 통해 바꾼 값들을 다시 정렬시켜줘야한다.
            # 최댓값 인덱스가 갱신되어 이전의 최댓값 인덱스 리스트에 없으면 다시 리스트 갱신
            if max_idx not in max_idx_list:
                max_idx_list = []
                for k in range(i, len(arr)):
                    if arr[k] == arr[max_idx]:
                        max_idx_list.append(k)

            # 이제 바꾼 값들에 대해 내림차순으로 정렬해서 갱신
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
            max_list = []
            for l in max_idx_list:
                max_list.append(arr[l])
            max_list.sort(reverse=True)
            for l in range(len(max_idx_list)):
                arr[max_idx_list[l]] = max_list[l]

            i += 1
            cnt += 1
        else:
            i += 1

    arr = "".join(arr)
    print(f'#{case} {arr}')
# counting sort

def counting_sort(input_arr, k):
    '''

    :param input_arr: 입력 받은 배열
    :param k: 데이터의 갯수가 아닌, 데이터 원소의 범위
    :return:
    '''

    count_arr = [0] * (k + 1) # 원소의 등장 횟수 기록

    # 원소 출현 빈도수 기록
    for i in range(len(input_arr)):
        count_arr[input_arr[i]] += 1

    # sort를 하는데, 중복된 원소가 여러번 등장할 경우, 등장한 순서도 알아야 할 필요가 있는 것
    # 등장 순서를 위해 counting_arr 가 업데이트
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    result_arr = [-1] * len(input_arr)
    
    # input_arr 에 정렬하여 값 할당하기 (count_arr 를 참조 할 것이다)
    for i in input_arr:
        count_arr[i] -= 1
        result_arr[count_arr[i]] = i

    return result_arr

arr = [0, 4, 3, 1, 1, 3, 1]

print(counting_sort(arr, 5))



















# while True:
#     sentence = str(input())
#     if sentence == '.':
#         break
#
#     balance = True
#     for i in range(len(sentence)):
#         for j in range(i, len(sentence)):

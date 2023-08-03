arr = ['Fish', 'And', 'Chip']
N = len(arr) # 배열의 길이

# arr 에 대한 모든 경우의 수
for i in range(1 << N):
    for j in range(N):
        if i & (1 << j):
            print(arr[j], end=', ')
    print()

    '''
    공집합
    Fish
    And
    Fish And
    Chip
    Fish Chip
    And Chip
    Fish And Chip
    '''

# 1 << 2 의 의미
N = 3
print(1 << N)
for case in range(1, 11):
    N = int(input())
    building_list = list(map(int, input().split()))
    
    house = 0
    # building 양 옆의 두개씩의 건물의 높이와 해당 건물 사이의 높이 차를 계산
    for building_idx in range(2, N - 2):
        b2 = building_list[building_idx] - building_list[building_idx - 2]
        b1 = building_list[building_idx] - building_list[building_idx - 1]
        a1 = building_list[building_idx] - building_list[building_idx + 1]
        a2 = building_list[building_idx] - building_list[building_idx + 2]
        # 그 높이 차들이 모두 어떤 high보다 클 때 house에 그 high값을 더해주면 세대의 수
        for high in range(256, 0, -1):
            if (high <= b2) & (high <= b1) & (high <= a1) & (high <= a2):
                house += high
                break
            
    print(f'#{case} {house}')
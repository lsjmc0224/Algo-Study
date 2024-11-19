'''
양동이의 개수 N
호스의 개수 M

둘째줄부터 M개의 줄 에 걸쳐 호스의 정보가 있음.

'''
N, M = map(int, input().split())

# 양동이 이어진 정보를 저장할 리스트
graph_info = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end = map(int, input().split())
    graph_info[start].append(end)

# 양동이 물 흘려보내기
def water_flow(N, graph_info):
    temp_water = [0] * (N + 1)
    temp_water[1] = 100  # 1번 양동이에 100만큼 물을 채운다
    
    # 1번부터 N번 양동이까지 순서대로 물 분배
    for i in range(1, N + 1):
        num_connected = len(graph_info[i])
        if num_connected == 0:
            continue
        divided_water = temp_water[i] / num_connected
        
        for j in graph_info[i]:
            temp_water[j] += divided_water
            temp_water[i] = 0

    return max(temp_water)

max_water = water_flow(N, graph_info)

print(f"{max_water:.6f}")

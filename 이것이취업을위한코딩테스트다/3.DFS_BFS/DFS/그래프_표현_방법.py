# Depth First Search : 깊이 우선 탐색

"""
graph = [[] for i in range(3)]
graph[0].append((1, 7))
"""

# graph : 탐색할 그래프, v = 처음 시작 노드,
def dfs(graph, v, visited):
    visited[v] = True  # 방문한 노드 = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:  # visited[i]의 값이 False이면 if 문 안의 조건문을 실행
            dfs(graph, i, visited)  # 재귀적으로 함수를 재호출


# 각 번호의 노드마다 연결되는 노드 번호 입력
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 5], [7], [2, 6, 8], [1, 7]]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False] * 9

print(dfs(graph, 1, visited))

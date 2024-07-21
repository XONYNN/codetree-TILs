from itertools import combinations

N, M = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] 
coms = list(combinations([0, 1, 2, 3], 2))
ANSWER = 0

for i in range(N):
    for j in range(M):
        for com in coms:
            r1 = com[0]
            r2 = com[1]

            new_x1, new_y1 = i + dx[r1], j + dy[r1]
            new_x2, new_y2 = i + dx[r2], j + dy[r2]

            if not 0 <= new_x1 < N: continue
            if not 0 <= new_x2 < N: continue
            if not 0 <= new_y1 < M: continue
            if not 0 <= new_y2 < M: continue

            ANSWER = max(ANSWER, G[i][j] + G[new_x1][new_y1] + G[new_x2][new_y2])

print(ANSWER)
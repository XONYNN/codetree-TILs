N, M, K = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
x, y = -1, -1

for i in range(N):
    for j in range(K-1, K+M-1):
        if x == -1 and y == -1:
            if G[i][j] == 1:
                x, y = i, j

for i in range(K-1, K+M-1):
    G[x-1][i] = 1

for line in G:
    print(*line, sep=" ")
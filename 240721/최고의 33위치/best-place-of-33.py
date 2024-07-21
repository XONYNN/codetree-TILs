N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
MAX = 0

for i in range(N-2):
    for j in range(N-2):
        cur = 0
        for x in range(3):
            for y in range(3):
                cur += G[i+x][j+y]
        
        if MAX < cur: MAX = cur

print(MAX)
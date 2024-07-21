N, M = map(int, input().split())
G1 = [list(map(int, input().split())) for _ in range(N)]
G2 = [[0] * N for _ in range(N)]
ANSWER = 0

for i in range(N):
    for j in range(N):
        G2[j][i] = G1[i][j]

for i in range(N):
    target1 = G1[i][0]
    target2 = G2[i][0]
    cnt1, cnt2 = 1, 1
    
    for j in range(1, N):
        if target1 != G1[i][j]:
            target1 = G1[i][j]
            cnt1 = 1
        else:
            cnt1 += 1
        
        if cnt1 == M:
            ANSWER += 1
            break

    for j in range(1, N):    
        if target2 != G2[i][j]:
            target2 = G2[i][j]
            cnt2 = 1
        else:
            cnt2 += 1
        
        if cnt2 == M:
            ANSWER += 1
            break
        
print(ANSWER)
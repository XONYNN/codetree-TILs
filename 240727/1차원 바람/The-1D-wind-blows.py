N, M, Q = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]

def shift(r, d):
    if d == 'L':
        C[r-1] = [C[r-1][-1]] + C[r-1]
        del C[r-1][-1]
    else:
        C[r-1] = C[r-1] + [C[r-1][0]]
        del C[r-1][0]

for _ in range(Q):
    r, d = input().split()
    r = int(r)

    shift(r, d)

    new_d = d
    for i in range(r-1, 0, -1):
        if new_d == 'L': new_d = 'R'
        else: new_d = 'L'

        for j in range(M):
            if C[i-1][j] == C[i][j]:
                shift(i, new_d)
                break
    
    new_d = d
    for i in range(r+1, N+1):
        if new_d == 'L': new_d = 'R'
        else: new_d = 'L'

        for j in range(M):
            if C[i-1][j] == C[i-2][j]:
                shift(i, new_d)
                break

for i in range(N):
    print(*C[i], sep=" ")
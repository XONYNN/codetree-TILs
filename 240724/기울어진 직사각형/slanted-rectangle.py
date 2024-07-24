def sum_value(load, G):
    value = 0

    for x, y in load:
        value += G[x][y]

    return value

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
MAX = -1

for i in range(2, N):
    for j in range(1, N-1):
        for k in range(2, i+1):
            for m in range(1, k):
                load = [(i, j)]
                cur_x, cur_y = i, j
                left, right = m, k-m

                if not 0 <= i - left  < N: continue
                if not 0 <= j - left  < N: continue
                if not 0 <= i - right < N: continue
                if not 0 <= j + right < N: continue

                for x in range(1, right+1):
                    cur_x, cur_y = cur_x - 1, cur_y + 1
                    load += [(cur_x, cur_y)]

                for x in range(1, left+1):
                    cur_x, cur_y = cur_x - 1, cur_y - 1
                    load += [(cur_x, cur_y)]               

                for x in range(1, right+1):
                    cur_x, cur_y = cur_x + 1, cur_y - 1
                    load += [(cur_x, cur_y)]
                
                for x in range(1, left):
                    cur_x, cur_y = cur_x + 1, cur_y + 1
                    load += [(cur_x, cur_y)]
                
                MAX = max(MAX, sum_value(load, G))
print(MAX)
N, T = map(int, input().split())
G1 = list(map(int, input().split()))
G2 = list(map(int, input().split()))

for i in range(T%(2*N)):
    G1 = [G2[-1]] + G1
    del G2[-1]
    G2 = [G1[-1]] + G2
    del G1[-1]

print(*G1, sep=" ")
print(*G2, sep=" ")
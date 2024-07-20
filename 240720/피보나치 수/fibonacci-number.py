N = int(input())
dp = [1, 1]

for i in range(N-2):
    dp += [dp[i] + dp[i+1]]

print(dp[-1])
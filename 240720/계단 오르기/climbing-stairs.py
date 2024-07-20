N = int(input())
dp = [1, 1, 1]

for i in range(N-4):
    dp += [dp[i] + dp[i+1]]

print(dp[N-2]%10007)
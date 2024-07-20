N = int(input())

dp = [1, 2]

for i in range(N-2):
    dp += [(dp[i] + dp[i+1]) % 10007]

print(dp[N-1])
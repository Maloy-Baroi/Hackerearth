n=int(input())

x=[int(i) for i in input().split()]

ans=1
for i in range(n):
    ans=(ans*x[i])%((10**9)+7)

print(ans)

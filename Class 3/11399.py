N = int(input())
num = list(map(int, input().split()))
sum = 0
num.sort()
for i in range(N):
    for j in range(i + 1):
        sum += num[j]
print(sum)

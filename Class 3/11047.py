N, K = map(int, input().split())

coin = []
count = 0
for _ in range(N):
    coin.append(int(input()))

coin.sort(reverse = True)

for i in coin:
    count += K//i
    K = K%i

print(count)

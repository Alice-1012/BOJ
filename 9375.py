from collections import Counter
N = int(input())
for i in range(N):
    n = int(input())
    cloth = []
    for j in range(n):
        a, b = input().split()
        cloth.append(b)
    num = 1
    result = Counter(cloth)
    for key in result:
        num *= result[key] + 1
    print(num - 1)

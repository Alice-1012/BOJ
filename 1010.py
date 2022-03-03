#ver.1
T = int(input())
def nCk(n,k):
    numerator = 1
    denominator = 1
    for i in range(1, k+1):
        denominator *= i
        numerator *= n+1-i
    return numerator/denominator
for _ in range(T):
    k, n = map(int,input().split())
    print(int(nCk(n,k)))
    
#ver.2
import math
T = int(input())

for _ in range(T):
    k, n = map(int,input().split())
    result = math.factorial(n) // (math.factorial(k)*math.factorial(n-k))
    print(result)
    
#ver.3
def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

T = int(input())

for _ in range(T):
    k,n = map(int, input().split())
    bridge = factorial(n) // (factorial(k) * factorial(n-k))
    print(bridge)

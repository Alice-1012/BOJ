from itertools import combinations

n,m = map(int, input().split())

card = list(map(int, input().split()))
com = list(combinations(card,3))
black = 0
for i in com:
  if sum(i) <= m:
    black = max(black, sum(i))
print(black)

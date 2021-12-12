a, b = map(int,input().split())

def f(n):
  new_num = str(n)[::-1]#[::-1] -> 처음부터 끝까지 -1칸씩 = 역순으로 재배치
  return(int(new_num))

if f(a) > f(b):
  print(f(a))
else:
  print(f(b))

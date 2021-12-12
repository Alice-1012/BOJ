T = int(input())

for i in range(T):
  r, s = input().split()

  for x in s:
    print(int(r)*x, end = '')#줄바꿈 없이 for문 입력받기 :end=''
  print()

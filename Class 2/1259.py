#1 기본 if-else 구조
while True:
  num = input()
  num_reverse = num[::-1]
  if num == '0':
    break
  elif num_reverse == num:
    print('yes')
  else:
    print('no')
    
#2 if-else 한줄 코드
while True:
  num = input()
  num_reverse = num[::-1]
  if num == '0':
    break
  else: 
    print('yes' if num == num_reverse else 'no')
    
==> 둘 다 시간, 메모리 사용은 같다

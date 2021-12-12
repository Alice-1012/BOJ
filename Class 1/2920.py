#1
num = input().split() #문자열 list
#asc_list = [1,2,3,4,5,6,7,8]은 숫자 list라서 error

asc_list = ['1','2','3','4','5','6','7','8'] 
des_list = list(reversed(asc_list))#list를 역순으로 뒤집어서 list로 반환

if num == asc_list:
  print('ascending')
elif num == des_list:
  print('descending')
else:
  print('mixed')
  
#2 
num = list(map(int,input().split()))

if num == sorted(num):
  print('ascending')
elif num == sorted(num, reverse = True):
  print('descending')
else:
  print('mixed')

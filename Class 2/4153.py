#1 num = map(int, input().split())
while True:
    num = map(int, input().split())
    if sum(num) == 0:
        break
    else:
        square = [x ** 2 for x in num]
        sortnum = sorted(square)
        print('right' if sortnum[0]+sortnum[1] == sortnum[2] else 'wrong')


#2 num = list(map()))
while True:
    num = list(map(int, input().split()))
    if sum(num) == 0:
        break
    else:
        square = [x ** 2 for x in num]
        sortnum = sorted(square)
        print('right' if sortnum[0]+sortnum[1] == sortnum[2] else 'wrong')

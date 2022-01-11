cnt = int(input())
stk = []

for i in range (cnt):
    num = int(input())
    if (num == 0):
        stk.pop()
    elif(num !=0):
        stk.append(num)
print(sum(stk))

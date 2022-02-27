A = ['SUN', 'MON','TUE','WED','THU','FRI','SAT']
B = [31,28,31,30,31,30,31,31,30,31,30,31]

m,n = map(int,input().split())
day = 0

for i in range(0,m-1):
    day += B[i]
day = (day+n)%7
print(A[day])

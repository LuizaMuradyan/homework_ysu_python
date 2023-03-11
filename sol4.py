1
summ = 0
for i in range(3):
    n = int(input('enter num: '))
    summ += n
print(summ)

2
b1 = int(input('enter b1: '))
q = int(input('enter q: '))
n = int(input('enter n: '))
print(f'b1 = {b1 * q ** (n-1)}')

3
n = int(input('enter the num: '))
if n % 2 == 0 :
    print(f'{n} is even')
else:
    print(f'{n} is odd')

4 
def is_arithmetic(listt):
    const = listt[1] - listt[0]
    for i in range(len(listt) - 1):
        if listt[i + 1] - listt[i] != const:
             return False
    return True

print(is_arithmetic([1, 2, 6, 4,5,2,3,4,5]))

5
n = int(input('n: '))
if len(str(n)) == 3:
    print('no')
elif n % 7 == 0 and n % 23 == 0:
    print('yes')
else:
    print('no')

6
import math
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if  b ** 2 - 4 * a * c < 0:
    print('no solution')
elif  b ** 2 - 4 * a * c == 0:
    print(-b / (2*a))
else:
    print(f'x1 = {(-b + math.sqrt(b ** 2 - 4 * a * c))/ (2*a)}\nx2 = {(-b - math.sqrt(b ** 2 - 4 * a * c))/ (2*a)} ')


8
n = int(input('n: '))
for i in range(1,11):
    print (f'n * {i} = {n * i}')

9 
new = []
lenn = int(input('enter the len(list): '))
for i in range(0,lenn):
    n = int(input('enter element: '))
    new.append(n)
print(new)


10
n = int(input('enter num: '))
for i in range(1,n//2 + 1):
    if n % i == 0:
        print(i)
print(n)


11
count = 0
new = []
lenn = int(input('enter the len(list): '))
for i in range(0,lenn):
    n = int(input('enter element: '))
    new.append(n)
for i in range(len(new)-1):
    if new[i+1] > new[i]:
        count += 1
print(count)

12
new = []
lenn = int(input('enter the len(list): '))
for i in range(0,lenn):
    s = input('enter element: ')
    new.append(s)
new.reverse()
print(new)

13
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(int(input('num: '))))

14
n = float(input('enter num: '))
for i in range(1,round(n ** 0.5) ):
    print(i ** 2)

15

n = int(input('enter num: '))
for i in range(0,n+1):
    if 2 ** i < n:
        print( 2 ** i)
       

16
def Power_of_two(n):
        return n > 0 and (n & (n - 1)) == 0
print(Power_of_two(64))

17
final = ''
while True:
    s = input('enter the word: ')
    if s == 'end' or s == 'End' or s == 'done' or s == 'Done' or s == 'Finish' or s == 'finish':
        print(final[0:-1])
    else:
        final += s
        final += ','
print(final)


18
summ = 0
listt = [-20,-10,-1,0,1,-5]
for i in listt:
    if i >= 0:
        print(summ)
        break
    else:
        summ += i

19
n = int(input('enter num: '))
n = str(n)[::-1]
print(int(n) * 2)

20
new = []
n = input('enter num: ')
for i in n:
    new.append(i)
if sorted(new) == new:
    print('yes!!!')
else:
    print('no!!!')
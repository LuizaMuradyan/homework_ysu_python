
1
n = int(input('enter num: '))
for i in range ( 2, n+1 ):
    if n % i == 0:
        print(i)
        break

2
new = []
count = 0
while True:
    n = int(input('enter num: '))
    if n != -1:
        new.append(n)
    else:
        break
maxi = max(new[:new.index(0)])
for i in new[:new.index(0)]:
    if i == maxi:
        count += 1
print(f'maximum is {maxi} and {count} times')

3
def func(lst):
    new = []
    for i in lst:
        if  i % 2 == 0 :
            continue
        elif i < 3 or i > 7 and i < 11 or i > 13 and i < 17 or i > 23:
            new.append(i)
    return new
print(func([12,9,6,0,1,-1,41,28,27,17]))

4
count = 0
text = 'Hi, Ann how are you doing?'
for i in text:
    if i == ' ':
        count += 1
print(count + 1)

5
s = ''
text = 'python is awesome'
text = text.split(' ')
for i in text:
    s += i 
    print(s)
    s = ''

6
path = input("Enter a Windows path: ")
linux_path = path.replace("\\", "/").replace("C:", "/home")
print("Linux path:", linux_path)

7
s = ''
for i in range(5):
    name = input('enter name: ')
    s += name
    s += '-->'
print(s[:-3])

8
new = []
n = int(input('how mane nums: '))
for i in range(n):
    num = int(input('num: '))
    new.append(num)
new.sort()
print(new)

9
a = [5,1,4,3,0,-1]
max, min = a.index(max(a)), a.index(min(a))
a[max], a[min] = a[min], a[max]
print(a)

10
n = int(input('num: '))
for i in range(1,n+1):
    if i > 1:
        print('')
    for j in range(1,i+1):
        print(j,end = '')

11
s = ''
n = int(input('enter count: '))
numbers = input('enter n nums with spaces: ')
numbers_list = numbers.split()
for i in numbers_list:
    if int(i[0]) > int(i[1]):  
        s += i[1] + i[0]
        s += ' '
    else:
        s += i[0] + i[1]
        s += ' '
s = s.split(' ')
print(sorted(s[:-1]))

12
result = 'yes'
n = int(input())
matrix = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][j] = int(input())
for i in range(n):
    for j in range(i+1,n):
        if matrix[i][j] != matrix[j][i]:
            result = 'no'
print(result)


13
s = ''
a = [3,7]
for i in range(a[0],a[1] + 1):
    s += str(i**2)
    s += ' '
print(s)

14
numbers = input("Enter a list of numbers separated by spaces: ")
numbers_list = numbers.split()
for i in numbers_list:
    print(int(i) ** 0.5)
    
15
numbers = input("Enter a list of numbers separated by spaces: ")
numbers_list = numbers.split()
for i in numbers_list:
    if int(i) % 2 == 0:
        print(int(i) ** 3, end = ' ')

16

for i in range(1,9):
    l = []
    for j in 'abcdefgh':
        l.append(j + str(i))
    print(*l)

17

h, w = map(int, input().split())
nums = [int(input()) for _ in range(h*w)]    
rows = [nums[i:i+w] for i in range(0, len(nums), w)]
for row in rows:
    print(*row)

18

n = int(input('anunneri qanak'))
names = ()
for i in range(n):
    name = input('anun: ').strip()
    names += (name,)  
print(names)

19
ls = []
n = int(input('anunneri qanak: '))
for i in range(n):
    name = input('anun: ')
    ls.append(set([name]))
unique_names = set().union(*ls)
print(unique_names)

kam


unique_names = set() 
n = int(input('Enter the number of names: '))
for i in range(n):
    name = input('Enter a name: ')
    unique_names.add(name)  
print(unique_names)

20
print(*sorted({word[-1] for word in input().split()}))






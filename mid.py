
1
def triangle(a, c='#'):
    new = []
    final = []
    for i in range(a):
            new += c * (i + 1) 
            final.append(new)
            new = []
    return final
print(triangle(3, '*'))
print(triangle(2))

2
def gcd(*numbers):
    if len(numbers) == 0:
        return None
    elif len(numbers) == 1:
        return numbers[0]
    else:
        a = numbers[0]
        b = gcd(*numbers[1:])
        return gcd_two_numbers(a, b)
def gcd_two_numbers(a, b):
    if b == 0:
        return a
    else:
        return gcd_two_numbers(b, a % b)
print(gcd(12, 18, 24))

3 
def fib(n, count):
    count[0] += 1 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1, count) + fib(n-2, count)
count = [0]
fib(10, count)
print("Number of function calls:", count[0])


4
def prime_factors(n):
    if n < 1:
        return []

    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i not in factors:
                factors.append(i)
    if n > 1 and n not in factors:
        factors.append(n)
    return factors
print(prime_factors(100))

5
def jumping_frog(P, h):
    for i in range(len(P)-1):
        if abs(P[i+1] - P[i]) > h:
            return "Game over"
    return "Frog wins"
print(jumping_frog([4,5,2],2))




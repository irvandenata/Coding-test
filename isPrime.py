def isPrime(n):
    if n == 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True


for i in range(1,101):
    if isPrime(i):
        print(i)

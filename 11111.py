def PrimeSum(m,n):
    sum = 0
    if 1<=m<n :
        for i in range(m,n+1):
            if prime(i) == True :
                sum += i
                print(i)
    return sum


def prime(p):
    for i in range(2 , p):
        if p % i == 0:
            return False
            break
        else:
           return True


m,n=input().split()
m=int(m)
n=int(n)
print(PrimeSum(m,n))
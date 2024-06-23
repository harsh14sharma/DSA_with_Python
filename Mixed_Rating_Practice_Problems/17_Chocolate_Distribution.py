t = int(input())
while t>0:
    n = int(input())
    if n % 3 == 0:
        x = n // 3 - 1
        print(x,x,n - 2 * x)
    elif n % 3 == 2:
        x = n // 3 + 1
        print(x,x,n - 2 * x)
    else:
        x = n // 3
        n = n - 2 * x
        print(x,x,n)
    t-=1

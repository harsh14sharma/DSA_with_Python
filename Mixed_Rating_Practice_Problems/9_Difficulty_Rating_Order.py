t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    # Your code goes here\
    for i in range(n-1):
        if(d[i]>d[i+1]):
            print("NO")
            break
    else:
        print("YES")
    t -= 1

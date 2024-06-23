# cook your dish here
t= int(input())
while t>0:
    n=int(input())
    a=list(map(int, input().split()))
    even=0
    for x in a:
        if(x% 2==0):
            even+=1
    odd = n - even
    if(odd%2==0 and odd>0):
        print("YES")
    else:
        print("NO")
    t-=1
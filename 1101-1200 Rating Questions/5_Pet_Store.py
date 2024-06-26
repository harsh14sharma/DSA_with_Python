# cook your dish here
t= int(input())
while t>0:
    n= int(input())
    a= list(map(int, input().split()))
    s=set(a)
    for i in s:
        if(a.count(i) % 2 !=0):
            print("NO")
            break
    else:
        print("YES")
    t-=1
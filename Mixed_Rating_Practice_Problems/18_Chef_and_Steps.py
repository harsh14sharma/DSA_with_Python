# cook your dish here
t= int(input())
while t>0:
    n,k= map(int,input().split())
    steps=list(map(int, input().split()))
    c=''
    for i in steps:
        if(i % k == 0):
            c+='1'
        else:
            c+='0'
    print(c)
    t-=1
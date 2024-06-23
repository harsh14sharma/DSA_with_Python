# cook your dish here
t= int(input())
while t>0:
    a,b,c,d = map(int ,input().split())
    l1= list(range(a,b+1))
    l2= list(range(c,d+1))
    count=len(l1)+len(l2)
    for i in l1:
        if (i in l2 ):
            count-=1
    print(count)
    t-=1
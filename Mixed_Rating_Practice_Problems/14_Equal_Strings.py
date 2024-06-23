# cook your dish here
t= int(input())
while t>0:
    n= int(input())
    a=input()
    b=input()
    l = []
    for i in range(n):
        if b[i] not in l and a[i]!=b[i]:
            l.append(b[i])
    print(len(l))
    t-=1
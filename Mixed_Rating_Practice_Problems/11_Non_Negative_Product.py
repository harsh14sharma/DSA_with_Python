# cook your dish here
t= int(input())
while t>0:
    n= int(input())
    a= list(map(int , input().split()))
    c=0
    for i in a:
        if(i < 0):
            c+=1
            if(c==2):
                c=0
        elif(i == 0):
            c=0
            break
    print(c)
    t-=1
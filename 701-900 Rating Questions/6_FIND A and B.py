test_case = int(input())
while test_case > 0:
    x,y,z = map(int , input().split())
    lst=list([x,y,z])
    A,B = 0,0
    for i in range(3):
        b,a=lst[i],1
        for j in range(3):
            if(i != j):
                a*=lst[j]
        if(a % b == 0):
            A,B =a , b
    if(A==0 and B==0):
        print(-1)
    else:
        print(A,B)
    test_case-=1
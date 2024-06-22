# cook your dish here
test_case = int(input())
while test_case >0:
    n ,k= map(int,input().split())
    lst = list(map(int , input().split()))
    m=0
    s=0
    for i in range(0,n-k+1):
        for j in range(i,i+k):
            s+=lst[j]
        if(m<s):
            m=s 
        s=0
    print(m)
    test_case-=1                    
    
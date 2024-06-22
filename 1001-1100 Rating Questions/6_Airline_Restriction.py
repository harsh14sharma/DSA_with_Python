# cook your dish here
test_case = int(input())
while test_case > 0:
    a,b,c,d,e= map(int , input().split())
    bag = list([a,b,c])
    flag=0
    for i in range(3):
        for j in range(3):
            if(i!=j and bag[i]+bag[j] <=d and bag[3-(i+j)]<=e):
                print("Yes")
                flag=1
                break
        if(flag==1):
            break 
    else:
        print("No")
    test_case-=1
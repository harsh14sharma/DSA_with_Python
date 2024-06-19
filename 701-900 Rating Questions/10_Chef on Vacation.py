# cook your dish here
test_case = int(input())
while test_case>0:
    x,y,z= map(int , input().split())
    if( x+ y <=z):
        print("YES")
    else:
        print("NO")
    test_case-=1
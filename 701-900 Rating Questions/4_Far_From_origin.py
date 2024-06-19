from math import sqrt
# cook your dish here
test_case = int(input())
while test_case > 0:
    x1,y1,x2,y2 = map(int , input().split())
    dist_alex , dist_bob = sqrt(x1*x1 + y1*y1),sqrt(x2*x2 + y2*y2)
    if(dist_alex > dist_bob):
        print("ALEX")
    elif(dist_alex < dist_bob):
        print("BOB")
    else:
        print("EQUAL")
    test_case-=1
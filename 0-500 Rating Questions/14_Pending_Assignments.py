# cook your dish here
test_case = int(input())
while test_case > 0:
    x,y,z = map(int , input().split())
    total_minutes = z*24*60
    total_time = x * y
    if(total_time <= total_minutes):
        print("YES")
    else:
        print("NO")
    test_case-=1
# cook your dish here
test_case = int(input())
while(test_case>0):
    a_min,b_min,c_min,t_min,a,b,c = map(int , input().split())
    if((a+b+c) >= t_min and a_min<= a and b_min <= b and c_min <= c):
        print("YES")
    else:
        print("NO")
    test_case-=1

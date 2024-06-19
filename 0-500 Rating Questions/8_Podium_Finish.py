# cook your dish here
test_case = int(input())
while test_case > 0:
    a,b = map(int, input().split())
    dist= a+b
    print(dist)
    test_case-=1
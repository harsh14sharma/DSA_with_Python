# cook your dish here
test_case= int(input())
while test_case > 0:
    n= int(input())
    group = list(map(int , input().split()))
    s=set(group)
    for i in s:
        if(group.count(i) % i != 0):
            print("No")
            break
    else:
        print("Yes")
    test_case-=1
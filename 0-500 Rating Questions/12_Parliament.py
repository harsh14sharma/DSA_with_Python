# cook your dish here
test_case = int(input())
while test_case > 0:
    resolution , favour= map(int ,input().split())
    
    if(favour >= resolution/2):
        print("YES")
    else:
        print("NO")
    test_case -=1 
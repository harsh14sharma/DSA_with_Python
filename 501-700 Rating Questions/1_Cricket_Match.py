# cook your dish here
test_case = int(input())
while (test_case > 0):
    runs , overs = map(int, input().split())
    if(runs <= (overs*6*6)):
        print("YES")
    else:
        print("NO")
    test_case-=1
# # cook your dish here
test_case = int(input())
while test_case>0:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    protein = 0
    count_days = 0
    for i in range(len(a)):
        if a[i]+protein < k:
            print("NO", i+1)
            break
        else:
            protein = (a[i]+protein) - k
            count_days += 1
    if count_days == len(a):
        print("YES")
    test_case -=1
    
    
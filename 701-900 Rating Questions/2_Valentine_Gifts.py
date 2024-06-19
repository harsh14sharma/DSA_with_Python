# cook your dish here
test_case = int(input())
while test_case > 0:
    budget=int(input())
    # 2^7 - 1 is the sum of a geometric series with 7 terms
    if(budget >= 2**7-1):
        print("YES")
    else:
        print("NO")
    
    test_case-= 1
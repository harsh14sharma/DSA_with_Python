# cook your dish here
test_case =int(input())

while (test_case > 0):
    pa,pb,qa,qb=map(int ,input().split())
    if(max(pa,pb) > max(qa,qb)):
        print("Q")
    elif(max(pa,pb) == max(qa,qb)):
        print("TIE")
    else:
        print("P")
    test_case -=1

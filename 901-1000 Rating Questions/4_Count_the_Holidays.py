# cook your dish here
test_case = int(input())
while (test_case >0):
    n=int(input())
    lst= list(map(int , input().split()))
    holidays=4*2
    for i in lst:
        #if(i not in [6,7,13,14,20,21,26,27]):
        #or
        if(i % 7 !=0 and (i%7)-6 !=0):
            holidays+=1
    print(holidays)   
    test_case-=1

# cook your dish here
test_case =int (input())
while(test_case >0):
    stat_a = list(map(int, input().split()))
    stat_b = list(map(int, input().split()))
    score_a=score_b=0
    for i in range(3):
        if(stat_a[i] > stat_b[i]):
            score_a+=1
        else:
            score_b+=1 
    if(score_a > score_b):
        print("A")
    else:
        print("B")
    test_case-=1
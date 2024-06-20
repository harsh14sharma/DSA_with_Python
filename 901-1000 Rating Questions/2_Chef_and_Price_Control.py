test_case = int(input())
while(test_case > 0):
    n,k = map(int,input().split())
    items = list(map(int,input().split()))
    total_price = sum(items)
    new_price =0
    for i in items:
        if(i > k):
            new_price+=k
        else:
            new_price+=i
    lost_price= total_price - new_price
    print(lost_price)
    test_case-=1
    
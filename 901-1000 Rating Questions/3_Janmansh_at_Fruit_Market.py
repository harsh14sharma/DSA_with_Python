# cook your dish here
test_case = int(input())
while( test_case > 0):
    x,a,b,c = map(int , input().split())
    items =list([a,b,c])
    min_price = 0
    count =0
    for _ in range(2):
        minimum = min(items)
        min_price+=minimum
        items.remove(minimum)
        count+=1
    min_price+=(x-2)*min(a,b,c)
    print(min_price)
    test_case-=1
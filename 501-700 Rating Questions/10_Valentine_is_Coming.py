# cook your dish here
test_case = int(input())
while test_case > 0:
    money,price = map (int , input().split())
    chocolates= money // price
    print(chocolates)
    test_case-=1

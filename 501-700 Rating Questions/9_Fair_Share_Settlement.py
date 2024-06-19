# cook your dish here
test_case = int(input())
while test_case > 0:
    payment, no_of_friends = map(int , input().split())
    average = payment // (no_of_friends+1)
    net_payment = payment - (no_of_friends * average)
    print(net_payment)
    test_case-=1
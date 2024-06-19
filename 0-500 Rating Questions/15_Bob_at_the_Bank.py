# cook your dish here

test_case =int(input())
while test_case >0:
    current , deposit , charge , months= map(int , input().split())
    total_balance = current + (months*(deposit - charge))
    print(total_balance)
    test_case-=1

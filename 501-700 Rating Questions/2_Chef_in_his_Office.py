# cook your dish here
test_case = int(input())
while test_case > 0:
    hours_1,hours_2 = map(int , input().split())
    total_hours = hours_1 * 4 + hours_2
    print(total_hours)
    test_case-=1
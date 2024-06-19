# cook your dish here
# no_of_friends // 4
test_case = int(input())
while test_case > 0:
    geyser , bucket = map(int , input().split())
    person= geyser // (bucket * 2)
    print(person)
    test_case-=1
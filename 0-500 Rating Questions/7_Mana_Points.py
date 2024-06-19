# cook your dish here
test_case = int(input())
while test_case > 0:
    mana_cost , mana_points = map(int , input().split())
    attack = mana_points // mana_cost
    print(attack)
    test_case-=1
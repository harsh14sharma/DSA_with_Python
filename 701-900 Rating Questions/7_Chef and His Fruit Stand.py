# cook your dish here
# cook your dish here
test_case = int(input())
while test_case > 0:
    x,y = map(int, input().split())
    if(x//2 <= y):
        no_of_fruit = x//2
    else:
        no_of_fruit= y//1
    print(no_of_fruit)
    test_case-=1
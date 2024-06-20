# cook your dish here
test_case = int( input())
while(test_case > 0):
    players , height = map(int , input().split())
    lst = list(map(int , input().split()))
    min_player=0
    for i in lst:
        if(i>height):
            min_player +=1
    print(min_player)
    test_case -=1
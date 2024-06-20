t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    streak_om= streak_addy = streak_max_om = streak_max_addy=0
    for i in a:
        if(i == 0):
            streak_om=0
        else:
            streak_om+=1
        if(streak_max_om < streak_om):
            streak_max_om = streak_om
    for i in b:
        if(i == 0):
            streak_addy=0
        else:
            streak_addy+=1
        if(streak_max_addy < streak_addy):
            streak_max_addy = streak_addy
    if(streak_max_addy > streak_max_om):
        print("Addy")
    elif(streak_max_om > streak_max_addy):
        print("Om")
    else:
        print("Draw")
    t -= 1
# Your code goes here

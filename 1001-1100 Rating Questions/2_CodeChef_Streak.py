t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    #we can solve this problem by using  function and also without function 
    
    # 1) by using  function 
    
    streak =streak_max=0 
    def check_max(a,streak_max,streak):
        for i in a:
            if(i == 0):
                streak=0
            else:
                streak+=1
            if(streak_max < streak):
                streak_max = streak
        return streak_max
    om=check_max(a,streak_max,streak)
    addy=check_max(b,streak_max,streak)
    if(addy > om):
        print("Addy")
    elif(om > addy):
        print("Om")
    else:
        print("Draw")
    t -= 1
    
    #or
    
    
    # 2) without function
    
    #streak_om= streak_addy = streak_max_om = streak_max_addy=0    
    # for i in a:
    #     if(i == 0):
    #         streak_om=0
    #     else:
    #         streak_om+=1
    #     if(streak_max_om < streak_om):
    #         streak_max_om = streak_om
    # for i in b:
    #     if(i == 0):
    #         streak_addy=0
    #     else:
    #         streak_addy+=1
    #     if(streak_max_addy < streak_addy):
    #         streak_max_addy = streak_addy
    # if(streak_max_addy > streak_max_om):
    #     print("Addy")
    # elif(streak_max_om > streak_max_addy):
    #     print("Om")
    # else:
    #     print("Draw")
    #
    
    


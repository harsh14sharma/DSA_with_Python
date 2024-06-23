# cook your dish here
t= int(input())
while t>0:
    a= list(map(int, input().split()))
    team_1= team_2=0
    for i in range(10):
        if(i%2 == 0 and a[i]==1):
            team_1+=1
        elif(i%2 != 0 and a[i]==1):
            team_2+=1
        else:
            pass
    if(team_1 > team_2):
        print(1)
    elif(team_2 > team_1):
        print(2)
    else:
        print(0)
    t-=1
    

# cook your dish here
t= int(input())
while t>0:
    day = list(map(int , input().split()))
    sunny=0
    rainy=0
    for i in day:
        if(i == 1):
            sunny+=1 
        else:
            rainy+=1 
    if(sunny > rainy):
        print("YES")
    else:
        print("NO")
    t-=1
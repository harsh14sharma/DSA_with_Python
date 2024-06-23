# cook your dish here
t=int(input())
while t>0:
    s=input()
    one = "ADOPQR"
    two ="B"
    zero = "CEFGHIJKLMNSTUVWXYZ"
    hole=0
    for i in s:
        if(i in two):
            hole+=2
        elif(i in one):
            hole+=1 
        else:
            hole+=0
    print(hole)         
    t-=1
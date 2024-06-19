# cook your dish here
test_case = int(input())
while test_case > 0:
    x,y,p,q= map(int, input().split())
    chef_point ,chefina_point= x+(p*10) , y+(q*10)
    if(chef_point > chefina_point):
        print("Chefina")
    elif(chef_point < chefina_point):
        print("Chef")
    else:
        print("Draw")
    test_case-=1
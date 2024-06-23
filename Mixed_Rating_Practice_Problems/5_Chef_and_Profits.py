# cook your dish here
t= int(input())
while t>0:
    x,y,z= map(int , input().split())
    profit = (x*z) - (x*y)
    print(profit)
    t-=1
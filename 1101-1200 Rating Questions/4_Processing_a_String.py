# cook your dish here
t= int(input())
while t>0:
    s= input()
    sum= 0
    for i in s:
        if(i in "0123456789"):
            sum+=int(i)
    print(sum)
    t-=1
t= int(input())
while t>0:
    n=int(input())
    def sum_parity(d):
        new=d
        s=0
        parity=''
        while (new>0):
            r=new %10
            s+=r 
            new//=10
        if(s %2 ==0):
            parity='even'
        else:
            parity='odd'
        return s,parity
        
    sum_n,parity_n=sum_parity(n)
    x=n+1
    while(x>n):
        sum_x,parity_x=sum_parity(x)
        if(parity_x != parity_n):
            break
        x+=1
    print(x)
    t-=1
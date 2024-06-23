# cook your dish here
t= int(input())
while t>0:
    n=int(input())
    fruit = list(map(int, input().split()))
    nutrition = list(map(int, input().split()))
    s=list(set(fruit))
    sum=0
    for i in range(len(s)):
        m=0
        for j in range(n):
            if( s[i]==fruit[j]):
                if (nutrition[j] > m):
                    m=nutrition[j]
        sum+=m
    print(sum)
    t-=1
    
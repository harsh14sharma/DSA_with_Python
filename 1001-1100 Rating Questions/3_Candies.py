# cook your dish here
test_case = int(input())
while test_case > 0:
    n=int(input())
    prices = list(map(int , input().split()))
    candy_1=[]
    candy_2=[]
    for i in prices:
        if( i not in candy_1):
            candy_1.append(i)
        elif(i not  in candy_2):
            candy_2.append(i)
        else:
            print("No")
            break
    if(len(candy_1)+len(candy_2) == len(prices)):
        print("Yes")
    test_case-=1
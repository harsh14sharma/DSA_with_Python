# cook your dish here
test_case = int(input())
while test_case >0:
    n,k=map(int , input().split())
    amount_lst= map(int, input().split())
    amount_left=k
    string=''
    for _ in amount_lst:
        if(amount_left >= _):
            string+='1'
            amount_left-= _
        else:
            string+='0'
    print(string)
    test_case-=1
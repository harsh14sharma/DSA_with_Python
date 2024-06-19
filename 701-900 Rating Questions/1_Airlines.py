# cook your dish here
test_case = int(input())
while test_case > 0:
    aircraft , passengers = map(int , input().split())
    if(passengers <= aircraft*100):
        need =0
    else:
        if(passengers % 100  == 0):
            need = (passengers - (aircraft * 100))// 100
        else:
            need=  (passengers - (aircraft * 100))// 100 +1
    print(need)
    test_case-=1

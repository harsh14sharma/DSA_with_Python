# cook your dish here
test_case =int(input())
while test_case >0:
    deal_1, deal_2 =map(int, input().split())
    evaluation_1,evaluation_2 = (deal_1*10) ,(deal_2 * 5)
    if(evaluation_1 > evaluation_2 ):
        print("FIRST")
    elif(evaluation_2 > evaluation_1):
        print("SECOND")
    else:
        print("ANY")
    test_case-=1

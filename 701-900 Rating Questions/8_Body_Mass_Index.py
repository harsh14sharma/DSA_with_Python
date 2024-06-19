# cook your dish here
test_case = int(input())
while test_case > 0:
    mass , height = map(int , input().split())
    bmi = mass/(height * height)
    if(bmi <= 18):
        print(1)
    elif(bmi in range(19,25)):
        print(2)
    elif(bmi in range(25,30)):
        print(3)
    else:
        print(4)
    test_case-=1
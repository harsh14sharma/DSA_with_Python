# cook your dish here
test_case = int(input())
while test_case > 0:
    n=int(input())
    start_time= list(map(int , input().split()))
    limit_time= list(map(int, input().split()))
    required_time = no_of_students= 0
    for _ in range(n):
        if (_ == 0):
            required_time = start_time[0]-0
        else:
            required_time = start_time[_] - start_time[_-1]
        if(required_time >= limit_time[_]):
            no_of_students+=1
    print(no_of_students)
    test_case-=1
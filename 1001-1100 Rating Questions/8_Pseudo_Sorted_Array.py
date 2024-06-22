# cook your dish here
test_case = int(input())
while test_case > 0:
    n= int(input())
    arr = list(map(int , input().split()))
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            arr[i],arr[i+1]=arr[i+1],arr[i]
            break
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            print("No")
            break 
    else:
        print("YES ")
    test_case-=1
# cook your dish here
test_case = int(input())
while test_case>0:
    disposable_mask ,cloth_mask = map(int ,input().split())
    if((disposable_mask * 100) > (cloth_mask * 10)):
        print("Cloth")
    elif((disposable_mask * 100) < (cloth_mask * 10)):
        print("Disposable")
    else:
        print("Cloth")
    test_case-=1


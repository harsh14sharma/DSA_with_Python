# cook your dish here
test_case = int(input())
while test_case > 0:
    x,y,z = map(int , input().split())
    population= x-y+z 
    print(population)
    test_case-=1

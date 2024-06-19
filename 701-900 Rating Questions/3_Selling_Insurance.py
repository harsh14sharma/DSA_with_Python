# cook your dish here
test_case = int(input())
while test_case > 0:
    cost_of_insurance = int(input())
    commission = 0.2 * cost_of_insurance
    if(100 % commission == 0):
        minimum_insurance = int(100 // commission)
    else:
        minimum_insurance = int(100 // commission +1)
    print(minimum_insurance)
    test_case-=1
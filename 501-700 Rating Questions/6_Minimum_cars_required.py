# cook your dish here
test_case =int(input())

while (test_case > 0):
    no_of_friends= int(input())
    if(no_of_friends % 4 == 0):
        no_of_cars=no_of_friends // 4
    else:
        no_of_cars = (no_of_friends //  4) +1
    print(no_of_cars)
    test_case -=1
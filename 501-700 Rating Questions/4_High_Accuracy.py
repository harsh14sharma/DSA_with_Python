# cook your dish here
test_case =int(input())
while test_case >0:
    marks = int(input())
    while(marks > 0):
        marks-=3
    incorrect = abs(marks)
    print(incorrect)
    test_case-=1

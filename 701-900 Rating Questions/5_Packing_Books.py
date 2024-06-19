# cook your dish here
test_case = int(input())
while test_case > 0:
    shelves , books, cardboard = map(int , input().split())
    if(books % cardboard == 0): 
        no_of_cardboard = shelves *(books // cardboard)
    else:
        no_of_cardboard = shelves *(books // cardboard +1)
    
    print(no_of_cardboard)
    test_case-=1
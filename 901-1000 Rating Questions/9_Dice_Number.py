# cook your dish here
test_case = int(input())
while( test_case > 0):
    lst=list(map(int , input().split()))
    score_alice=score_bob =''
    for i in range(int(len(lst)//2)):
        score_alice+=str(max(lst[0:int(len(lst)//2)]))
        score_bob+=str(max(lst[int(len(lst)//2):len(lst)]))
        lst.remove(max(lst[0:int(len(lst)//2)]))
        lst.remove(max(lst[int(len(lst)//2):len(lst)]))
    if(score_alice > score_bob):
        print("Alice")
    elif(score_bob > score_alice):
        print("Bob")
    else:
        print("Tie")
    test_case-=1 
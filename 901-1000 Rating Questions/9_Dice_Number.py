# cook your dish here
test_case = int(input())
while( test_case > 0):
    lst=list(map(int , input().split()))
    lst_alice=lst[0:3]
    lst_bob=lst[3:6]
    score_alice=score_bob =''
    # for i in range(int(len(lst)//2)):
    #     score_alice+=str(max(lst[0:int(len(lst)//2)]))
    #     score_bob+=str(max(lst[int(len(lst)//2):len(lst)]))
    #     lst.remove(max(lst[0:int(len(lst)//2)]))
    #     lst.remove(max(lst[int(len(lst)//2):len(lst)]))
    for i in range(len(lst_alice)):
        score_alice+=str(max(lst_alice))
        score_bob+=str(max(lst_bob))
        lst_alice.remove(max(lst_alice))
        lst_bob.remove(max(lst_bob))
        
    if(int(score_alice) > int(score_bob)):
        print("Alice")
    elif(int(score_bob) > int(score_alice)):
        print("Bob")
    else:
        print("Tie")
    test_case-=1 
t = int(input())

while t > 0:
    n = int(input())
    s = input()
    server="alice"
    receiver="bob"
    score_alice=0
    score_bob=0
    for i in s:
        if( i== "A" and server=="alice"):
            score_alice+=1
        elif(i=="A" and server != "alice"):
            server="alice"
        elif(i=="B" and server=="bob"):
            score_bob+=1
        else:
            server="bob"
    print(score_alice , score_bob)        
    # Your code goes here
    t -= 1

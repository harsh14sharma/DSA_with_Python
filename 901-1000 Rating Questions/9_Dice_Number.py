lst=list(map(int , input().split()))
score_alice=max(lst[0:3])
score_bob = max(lst[3:6])
print(score_alice , score_bob)
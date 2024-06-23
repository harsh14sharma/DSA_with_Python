t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    s=set(a)
    m1 = max(s)
    s.remove(m1)
    m2=max(s)
    print(m1+m2)
    t -= 1
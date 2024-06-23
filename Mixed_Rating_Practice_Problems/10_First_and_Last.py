# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    max_sum = 0
    for i in range(n):
        s = a[i] + a[(i + n - 1) % n]
        if s > max_sum:
            max_sum = s
            
    print(max_sum)

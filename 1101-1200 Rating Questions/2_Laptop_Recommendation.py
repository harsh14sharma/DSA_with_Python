t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    counts = [0] * 10
    
    for i in range(n):
        counts[a[i] - 1] += 1
        
    m = max(counts)
    
    if counts.count(m) == 1:
        laptop = counts.index(m) + 1
        print(laptop)
        
    else:
        print("CONFUSED")
            
            
    t -= 1

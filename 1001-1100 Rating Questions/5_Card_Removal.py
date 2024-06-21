# Read number of test cases
test_case = int(input())
while test_case > 0:
    n = int(input())
    cards = list(map(int, input().split()))
    d = {}
    for _ in cards:
        if _ not in d:
            d[_] = cards.count(_)
    m = max(d.values())
    moves = n - m
    print(moves)
    test_case-=1

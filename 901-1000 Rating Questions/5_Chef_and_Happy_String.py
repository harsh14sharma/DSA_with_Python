t = int(input())

while t > 0:
    s = input()
    count=0
    vowels=['a','e','i','o','u']
    for _ in range(len(s)-2):
        if ((s[_] in vowels) and (s[_+1] in vowels) and (s[_+2] in vowels)):
            print("HAPPY")
            break
        
    else:
        print("Sad")
            
    # Your code goes here
    t -= 1

# cook your dish here
test_case = int(input())
while test_case >0:
    n = int(input())
    s= input()
    time =0
    i=0
    while(i < len(s)):
        if(i!=len(s)-1 and s[i]!=s[i+1]):
            time+=1
        elif(i!=len(s)-1 and s[i]==s[i+1]):
            time+=1
            i+=1
        else:
            time+=1
            
        i+=1
    print(time)
    test_case -=1
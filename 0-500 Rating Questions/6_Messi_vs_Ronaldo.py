# cook your dish here
mg,ma,rg,ra=map(int , input().split())
messi = mg * 2 + ma
ronaldo = rg*2 + ra
if(messi > ronaldo):
    print("Messi")
elif(ronaldo > messi):
    print("Ronaldo")
else:
    print("Equal")
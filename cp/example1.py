input_=input().split()
n=int(input_[0])
k=int(input_[1])
m=list(map(int, input().split()))
s=set(m)
c=0
for j in m:
    if j-k in s:
        c=c+1
print(c)

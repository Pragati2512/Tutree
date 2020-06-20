def palindrome(a):
    return a==a[::-1]

inp= str(input())
small=[]
capital=[]
num=[]

for i in inp:
    if(i.isdigit()):
        num.append(i)
    elif(i.islower()):
        small.append(i)
    else :
        capital.append(i)    

num.sort()
small.sort()
capital.sort()

ans=""
a=0
b=0
c=0

for i in inp:
    if(i.isdigit()):
        ans=ans+num[a]
        a=a+1
    elif(i.islower()):
        ans=ans+small[b]
        b=b+1
    else :
        ans=ans+capital[c]
        c=c+1

print(ans)





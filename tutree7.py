def isPrime(num):
    if(num==1):
        return 0
    flag=1
    for i in range(2,num):
        if((num%i)==0):
            flag=0
            break
    return flag    


inp= int(input())
ans = 0
for i in range(1,inp):
    if(isPrime(i) and isPrime(inp-i)):
        print(str(i)+" " + str(inp-i))
        ans=1
        break

if(ans==0):
    print("-1")        
 
        

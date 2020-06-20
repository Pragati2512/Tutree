list1 = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
list2=list1
K=2

subs=len(list1)-K +1

for i in range(0,subs,K):
    print(list2[i:i+K])
    list2=list1

list1.reverse()

for i in range(0,subs,K):
    print(list2[i:i+K])
    list2=list1
    

list1 = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
list2=list1
ans_list=[]
K=4

subs=len(list1)-K +1

for i in range(0,subs):
    ans_list.append((max(list2[i:i+K])))
    list2=list1


print(ans_list)

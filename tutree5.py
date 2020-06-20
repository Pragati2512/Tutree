string= input("Enter any string ")
vowels=['a', 'e', 'i', 'o','u']
newstr=""
for c in string:
    if c in vowels:
        newstr = newstr + c
print("Ans- " + newstr)

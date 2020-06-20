def palindrome(a):
    return a==a[::-1]

a = str(input())
ans=palindrome(a)

if ans:
    print("is palindrome")
else:
    print("not palindrome")

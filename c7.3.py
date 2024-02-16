# Write a program to print given number is a Palindrome number or not.

n=int(input('Enter a Number:'))
t=n
s=0
while n!=0:
    r=n%10
    s=(s*10)+r
    n=n//10
if(t==s):
    print('Palindrome Number')
else:
    print('Not an Palindrome Number')

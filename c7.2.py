# Write a program to print given number is armstrong number number or not.

n=int(input('Enter a number:'))
t=n
s=0
while n!=0:
    r=n%10
    s=s+(r*r*r)
    n=n//10
if(t==s):
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')
    

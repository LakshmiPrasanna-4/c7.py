# Write a program to print given number is prime or not.

n=int(input('Enter a Number:'))
c=0
i=1
while(i<=n):
    if n%i==0:
        c=c+1
    i=i+1
if c==2:
    print('Prime Number')
else:
    print('Not a Prime Number')

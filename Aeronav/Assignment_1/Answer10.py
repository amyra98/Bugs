
x=int(input('Enter a number: '))
y=int(bin(x)[2:])
z=str(y)[::-1] 
if int(z)==y:
    print("Binary of a given decimal number is a palindrome.")
else:
    print("Binary of a given decimal number is not a palindrome.")
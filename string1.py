boo = input ("Put in the number")

#Let's convert boo to interger
boo_integer = int(boo)
print(boo_integer%2)
#the program has to print if the number from user is odd or even
if(boo_integer%2)==0:
    print("even")
else:
    print("odd")

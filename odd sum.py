n=input("put in number")
n_int=int(n)
odd_coll=0
for odd in range(1,n_int+1,2): # 1 3
    odd_coll=odd_coll+odd
print(odd_coll)

n=input("put in number")
n_int=int(n)  # 5
b_int=1 #5
sign = +1

#1-3 3-1
while(True):
      print(b_int)
      b_int= b_int+1*sign
      if (b_int==n_int):
            #something happens to start count DOWN
            sign = -1
      if(b_int==0):
            break





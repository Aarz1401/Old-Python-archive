def collatz(num):
  iterations =0
  while num!=1:
    if num%2 ==0:
        num = num//2
        iterations += 1

    elif num%2==1:
        num=num*3 +1
        iterations+=1
    print(num,end=",")
  return iterations


try:
     n=int(input("Enter positive integer to apply the collatz function on:"))
     if n<=0:
         print(" 0 and Negative  values are not accepted")

     else:
         print("\nnumber of iterations=",collatz(n))
except ValueError:
    print("Invalid integer")

#WOW MATHEMATICAL MIRACLE




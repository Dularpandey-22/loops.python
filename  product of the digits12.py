n=int(input("enter number"))
product=1
while n>0:    
    product=product*(n%10)    
    n=n//10    
print("product of digits=",product)
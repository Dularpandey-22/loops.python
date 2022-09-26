n=int(input("enter the number"))
i=1
count=0
while i<=n:
    if i%2==0:
        print("even number is",i)
        count=count+1
    else:
        print("odd numner is",i)
        coun=count+1
    i=i+1
print("your count even number is",count)
print("your count odd number is",coun)
#to get marks form user
a=int(input("Enter a value"))
b=int(input("Enter b value"))
c=int(input("Enter c value"))
if(a>b and a>c):
   if(b>c):
       print("a and b is bigger")
       print("the avg of both is",(a+b)/2)
   else:
       print("a and c is bigger")
       print("the avg of both is",(a+c)/2)
elif(b>c and b>a):
    if(a>c):
        print("a and b is bigger")
        print("the avg of both is",(a+c)/2)
    else:
        print("b and c is bigger")
        print("the avg of both is",(b+c)/2)
else:
    if(a>b):
        print("a and c is bigger")
        print("the avg of both is",(a+c)/2)
    else:
        print("b and c is bigger")
        print("the avg of both is",(b+c)/2)

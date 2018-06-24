num=1
while (num!=0):
 print ("MENU-")
 print "1.check no is prime or not"
 print "2. check no is armstrong or not"
 print "3. find factorial of the number"
 print "4. exit"
 num2=input('enter your choice:')
 if num2==4:
     num=0
 while(num2!=4):
     num1= input('enter a number:')
 def prime(num1):
  temp=num1
  if temp==2:
      return 1
      exit()
  for x in range(2,temp):
    if temp%x == 0:
       return 0
    else:
        return 1
 y= prime(num1)
 if num2==1:
    if(y==1):
     print 'prime'
    else:
     print 'not prime'

 def armstrong(num1):
    s=0
    temp=num1
    while(temp!=0):
      dig=temp%10
      temp=temp/10
      cube=dig**3
      s=s+cube
    if s==num1:
      return 1
    else:
      return 0
 z=armstrong(num1)
 if num2==2:
      if(z==1):
        print 'no is armstrong'
      else:
        print 'no is not armstrong'
 
 def factorial(num1):  
    if(num1==0):
        return 1
    if (num1==1):
        return 1
    else:
        return num1*factorial(num1-1)
 a=factorial(num1)
 if num2==3:
     print 'factorial of',num1,'is',a

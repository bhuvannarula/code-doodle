'''
Code to print pattern according to numbers given.
eg.
  input ->   3,5,6
  output ->      *
               * *
               * *
             * * *
             * * *
             * * *
'''
  
x=eval("["+input("Enter Numbers with comma: ")+"]")
z=max(x)
for i in range(z,0,-1):
    for j in range(0,len(x)):
        if x[j]<i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

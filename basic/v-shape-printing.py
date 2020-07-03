'''
Code to print the smaller string as it is and larger string as:
            E     E
             X   L
              A P
               M
'''

a=input("Enter a Word: ")
b=input("Enter a Word: ")
print(b if len(a)>=len(b) else a)
x= " "+ (a if len(a)>=len(b) else b)                                #space is added so that first element starts from index(1).
print(x)                      
z=int((len(x))/2)                                                   #determines the number of rows to be printed.
for i in range(1,z+1):
    if x[i]==x[-i] and i==z and len(x)%2==0:                        #condition when only one element to be printed in last row.
        print(" "*(i-1),x[i],sep="")
    else:
        print(" "*(i-1),x[i]," "*(len(x)-(1+2*i)),x[-i],sep="")

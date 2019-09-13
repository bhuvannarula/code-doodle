y=input("Enter the long string:")
x=input("Enter string to be found:")
a=0
while y.find(x)!=-1:
    a+=1
    y=y[(y.find(x)+1):len(y)]
print("No. of Occurences:",a)

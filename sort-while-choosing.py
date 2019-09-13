'''
This code sorts the data while choosing (main aim).
'''

x=eval("["+input("Enter with comma: ")+"]")         #to accept more than 2 digit no.
y=eval("["+input("Enter with comma: ")+"]")
x.sort()
y.sort()
for i in x:
    s=0
    for j in y:
        if j>=i:
            y.insert(s,i)                           #editing the original list
            break
        s+=1
print(y)

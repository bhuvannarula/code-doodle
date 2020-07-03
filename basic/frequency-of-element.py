'''
Code to find frequency of an element in a list

Note: input to be given in the following format:
        1,2,3,4
        
        strings are not allowed for now.
'''

p,q,r=[],[],[]
p=eval("["+input("Enter Values sep with comma: " )+"]")
p.sort()
for i in p:
    if i in q:
        r[q.index(i)]+=1
    else:
        q.append(i)
        r.append(1)
for i in range(0,len(q)):
    print("Frequency of '",q[i],"' is ",r[i],sep="")

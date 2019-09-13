'''
Code to find longest substring of consonants
  Eg.     "hellowrld"
   Output-> "wrld"
'''

x=input("Enter String: ")
p,j,r='',0,list("AEIOUaeiou")
for i in range(0,len(x)):
    q=''
    while i<len(x) and x[i] not in r:
        q+=x[i]
        i+=1
    if len(q)>=j:
        j=len(q)
        p=q
print(p)
        

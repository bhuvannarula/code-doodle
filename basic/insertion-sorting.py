'''
4,7,2,8,5,1,5
4,7
2,4,7,8,5,1,5


        
        

'''
d=eval("["+input("Enter with comma: ")+"]")

print("Insertion Sort")
for i in range(1,len(d)):
    t=d[i]
    for j in range(i,-1,-1):
        print(d)
        print(i,j)
        if j==0 and d[0]>t:
            d[0],d[1]=t,d[0]
        elif j==i:
            continue    
        elif d[j]>=t:
            d[j+1]=d[j]
        elif d[j]<t:
            d[j+1]=t
            break
print("The Sorted List is:",d)

'''
Code to print the following arrangement:
                  1 
                1 2 1 
              1 2 3 2 1 
            1 2 3 4 3 2 1 
          1 2 3 4 5 4 3 2 1
'''

x=[1,2,3,4,5]
y=[]
for i in x:
    y.insert(len(y)//2,i)
    print("  "*int(x[-i]),end="")
    for k in y:
        print(k,end=" ")
    print()
    y.insert(len(y)//2,i)

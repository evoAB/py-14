l=[4,"abc","ios",5,3.14,6,8]
l1=[]
for i in l:
    if type(i)==int:
        l1.append(i)
l=l1
print(l)
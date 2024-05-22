lst=[10,501,22,37,100,999,87,351]
lst1=[]
lst2=[]
for i in lst:
    if i%2==0:
        lst1.append(i)
    elif i%2!=0:
        lst2.append(i)
print(lst1)
print(lst2)
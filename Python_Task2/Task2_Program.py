my_lst=[10,501,22,37,100,999,87,351]
new_lst=[]
for i in my_lst:
    cnt=0
    for j in range(1,i):
        if i%j==0:
            cnt+=1
    if cnt==1:
        new_lst.append(i)
print(new_lst)
def common(lst1,lst2,lst3):
    duplicates=[]
    for ele in lst1:
        if ele in lst2 and ele in lst3:
            duplicates.append(ele)
    return duplicates
lst1=[1,4,45,56,3,9]
lst2=[23,32,1,56,7,55]
lst3=[98,1,33,56,78]
duplicates=common(lst1,lst2,lst3)
print(duplicates)
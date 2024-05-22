lst= [10,501,22,37,100,999,87,351]
new_lst = []
def happy(a):
    for i in range (len(a)):
        sum = lst[i]
        while sum!=1 and sum !=4:
            tem_sum = 0
            for digit in str(sum):
                tem_sum += int(digit) ** 2
                sum = tem_sum
                if sum == 1:
                    new_lst.append(lst[i])
                    return new_lst
print(happy(lst))
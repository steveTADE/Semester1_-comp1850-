
def func_1(lst_value : list): 
    ''' 
    the mean of the list of value
    ''' 
    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
        sum = sum + value 
    return sum/num_of_value 
print(func_1([i + 1 for i in range(10)]))
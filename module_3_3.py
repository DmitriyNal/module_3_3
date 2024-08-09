def print_params(value,_str,_float):
    print(value,_str,_float)


values_list=[78,'ball',9.787]#исходный первый список
values_dict={'value':56,'_str':78,'_float':7.98}#исходный словарь
values_list_2 = [54.32, 'Строка' ]#исходный второй список


print_params(*values_list)# распаковка первого списка
print_params(**values_dict)#распаковка словаря
print_params(*values_list_2,42) #распаковка второго списка





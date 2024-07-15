
def print_params(a = 1, b = 'строка', c = True): #*args **kwargs
    print(a,b,c)

print_params()

print_params(b = 25)
print_params(c = [1,2,3])



values_list = [1, 'строка', True]
values_dict = {'a':1, 'b': 'строка', 'c': True}
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)

print_params(*values_list)
print_params(**values_dict)


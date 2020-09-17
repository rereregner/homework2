my_int = 5
my_float = 1.2
my_str = "Hello world"
my_list = ['a', '2']
my_tuple = ('b', '3')
my_dict = {'city': 'Tomsk', 'country': 'Russia'}

super_list = [my_int, my_float, my_str, my_list, my_tuple, my_dict]
for i in super_list:
    print(f'{i} is {type(i)}')

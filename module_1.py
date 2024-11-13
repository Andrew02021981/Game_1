import importlib
m = int(input('Введите количество игр от 1 до 5:'))
dict_1={}
for i in range (1,m+1):
    print('Введите имя',i,'игрока:')
    name = input()
    import module_2
    if i > 1:
        importlib.reload(module_2)
    from module_2 import counter
    dict_1.update({name:counter})

min_value = min(dict_1.values())
win_dict = {k: v for k, v in dict_1.items() if v == min_value}
keys, values = zip(*win_dict.items())
print('Ура! Наш победитель', *keys, sep=', ')
print('с результатом', *set(values), 'хода(-ов)!')


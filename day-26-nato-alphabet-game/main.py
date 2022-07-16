# name = 'Angela'
# new_list = [letter for letter in name]

# num_list = [n*2 for n in range(1,5)]
# print(num_list)

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

caps_list = [name.upper() for name in names if len(name) > 5]
print(caps_list)

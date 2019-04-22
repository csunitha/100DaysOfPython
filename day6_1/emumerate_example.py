''' enumerate function '''

menu_items = ['apple', 'orange', 'potato', 'lemondrops']

# you need to iterate over a list and keep track of
# the position of each element. For example, if you need to display
# menu items in a shell, you can simply use the range function

#WEONG way
print('printing using range...')
for menu_i in range(len(menu_items)):
    menu_item = menu_items[menu_i]
    print("{}.{}".format(menu_i, menu_item))

#right way
print('\n\nprinting using enumeration...')
for menu_i, menu_item in enumerate(menu_items):
    print("{}.{}".format(menu_i, menu_item))
   

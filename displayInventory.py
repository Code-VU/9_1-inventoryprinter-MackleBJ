stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    print('Inventory:')
    total_items = 0
    for key in stuff:
        print(stuff[key], key)
        total_items += stuff[key]
    
    print('Total number of items: {}'.format(total_items))


displayInventory(stuff)
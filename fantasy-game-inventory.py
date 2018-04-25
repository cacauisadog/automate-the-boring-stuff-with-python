def display_inventory(inventory):
    total_items = 0
    print('Inventory:')
    for k, v in inventory.items():
        print('%i %s' % (v, k))
        total_items += v
    print('Total number of items: %i' % total_items)

def add_to_inventory(inventory, loot):
    for item in loot:
        if item in inventory.keys():
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
display_inventory(inventory)
add_to_inventory(inventory, dragon_loot)
print('\nAfter dragon loot: \n')
display_inventory(inventory)

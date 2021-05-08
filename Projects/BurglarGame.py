'''This is a burglar game'''
#Introduction
print('Welcome to Burglar Game.')
print('Suppose you break into a house and you have only 1 minute to decide what to take and escape.')
print('What do you choose?')

import time
import item

def build_house_items(item_name, item_value, item_weight):
    """Return a list of items found in the house"""
    item_list = []
    for count in range(len(item_name)):
        item_list.append(item.Item(item_name[count], item_value[count], item_weight[count]))
    return item_list 

def greedy_solutions(item_list, keyFunction, player):
    """Return greedy solutions, one by one:
    - By value
    - By density
    - By weight
    """
    item_to_take = []
    item_list_sort = sorted(item_list, key = keyFunction, reverse = True)
    total_capacity = 0
    for element in item_list_sort:
        if total_capacity + element.getWeight() <= player.getCapacity():
            item_to_take.append(element)
            total_capacity += element.getWeight()
            player.updateMoney(element.getValue())
        player.updateCapacity(total_capacity)
    return item_to_take

def decision_tree(item_list, capacity):
    """Assumes item_list: a list of items, capacity.
    Returns a tuple of the total value of a
    solution to 0/1 knapsack problem and
    the items of that solution"""
    if item_list == [] or capacity <= 0:
        result = ([], 0)
    elif item_list[0].getWeight() > capacity:
        result = decision_tree(item_list[1:], capacity)
    else:
        nextItem = item_list[0]
        toTake, withVal = decision_tree(item_list[1:], capacity - nextItem.getWeight())
        withVal += nextItem.getValue()
        notToTake, withoutVal = decision_tree(item_list[1:], capacity)
        if withVal > withoutVal:
            result = (toTake + [nextItem], withVal)
        else:
            result = (notToTake, withoutVal)
    return result
def powerSet(items):
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        combo1 = []
        combo2 = []
        for j in range(N):
            # test bit jth of integer i
            if (i // 3**j) % 3 == 1:
                combo1.append(items[j])
            elif (i // 3**j) % 3 == 2:
                combo2.append(items[j])
        yield (combo1,combo2)






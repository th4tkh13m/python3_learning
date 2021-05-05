#Brute Force and Dynamic Programming
def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    # Your code here
    N = len(items)
    for i in range(3**N):
        combo1 = []
        combo2 = []
        for j in range(N):
            # test bit jth of integer i
            if (i // 3**j) % 3 == 1:
                combo1.append(items[j])
            elif (i // 3**j) % 3 == 2:
                combo2.append(items[j])
        yield (combo1, combo2)

# generate all combinations of N items
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo

#Graph Problems
nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)
    
# Write the code that adds the appropriate edges to the graph
# in this box.
for x in nodes:
    for y in nodes[1:]:
        if x.getName() == y.getName() or len(x.getName()) != len(y.getName()) :
            continue
        else:
            good_dif = 0
            bad_dif = 0
            count = 0
            while count < len(x.getName()):
                if x.getName()[count] != y.getName()[count]:
                    print(x,y)
                    good_dif += 1
                    if x.getName()[count] != y.getName()[count + 1] or y.getName()[count] != x.getName()[count + 1] or good_dif > 1:
                        bad_dif += 1
                        break
                    else:
                        count += 1
                count += 1
            if bad_dif != 0 or good_dif > 1:
                continue
            else:
                if y not in g.childrenOf(x):
                    g.addEdge(Edge(x,y))
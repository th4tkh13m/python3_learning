def generator1():
    if True:
        yield 1 

def generator2():
    if False:   
        yield 1

g1 = generator1()
g2 = generator2()

print(type(g1))
print(type(g2))
print(next(g1))
print(next(g2))
def allDiv(num):
    return sum(map(lambda x: num % x == 0, range(1, 21))) == 20
x = 20
while(not allDiv(x)):
    x += 20
print x

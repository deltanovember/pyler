max = 0
for i in range(0, 1001):
    for j in range(0, 1001):
        if ((lambda x:str(x) == str(x)[::-1])(i*j) and i*j > max):
            max = i*j
print max
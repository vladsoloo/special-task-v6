from random import randint
a = [randint(0, 101) for i in range(50)]
a.append(100)
print(a)
if 77 in a:
    print('Yes')
else:
    print('No')

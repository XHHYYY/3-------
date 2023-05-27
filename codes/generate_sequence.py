from random import randint
import typing

txt = ''
m = 20
arrive = 0
for i in range(1, m+1):
        require_mem = randint(1, 512)
        arrive = arrive + randint(1, 5)
        require_time = randint(1, 20)
        txt += '{} {} {} {}\n'.format(*list(map(str, [require_mem, i, arrive, require_time])))
print(txt)
with open('./codes/sequence.txt', 'w') as f:
    f.write(txt)

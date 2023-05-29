from random import randint


def generate():
    txt = ''
    list_len = 10
    arrive = 0
    for i in range(1, list_len+1):
        require_mem = randint(1, 512)
        arrive = arrive + randint(1, 5)
        require_time = randint(1, 20)
        txt += '{} {} {} {}\n'.format(*list(map(str,
                                      [require_mem, i, arrive, require_time])))
    with open('./codes/sequence.txt', 'w') as f:
        f.write(txt)


if __name__ == '__main__':
    generate()

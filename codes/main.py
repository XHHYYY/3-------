from Classes import Memory, process
from CPU import CPU
from Algorithms import First_fit

def read_sequence() -> list:
    with open('./codes/sequence.txt', 'r') as f:
        txt = f.read()
    requirement_list:list[process] = []
    list_sequence = txt.split('\n')
    for requirement in list_sequence:
        if requirement == '':
            break
        temp = list(map(int, requirement.split()))
        p = process(*temp)
        requirement_list.append(p)
    return requirement_list


def search(head:Memory, num:int) -> Memory:
    cur = head
    while(cur.next != None):
        if cur.next.mem_num == num:
            return cur.next
        else:
            cur = cur.next
            continue
    raise Exception('Memory not found')


def linked_list_init() -> Memory:
    init = Memory()
    head = Memory(-1, False, -1, 0, init)
    init.prev = head
    del init
    return head

if __name__ == '__main__':
    head = linked_list_init()
    requirements = read_sequence()
    CPU(head, requirements, First_fit)
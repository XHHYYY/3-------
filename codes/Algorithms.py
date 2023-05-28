from Classes import Memory, process
import typing


def First_fit(head:Memory, p:process) -> typing.Tuple[bool, Memory or None]:
    cur = head
    assert isinstance(cur, Memory)
    while(cur != None):
        if cur.is_free and cur.size >= p.need_mem:
            return (True, cur.allocate_mem(p.need_mem))
        cur = cur.next
    return (False, None) # type: ignore

def Next_fit(cur_pointer:Memory, p:process) -> typing.Tuple[bool, Memory or None, Memory]:
    cur_pointer = cur_pointer.next # type: ignore
    assert isinstance(cur_pointer, Memory)
    while(cur_pointer != None):
        if cur_pointer.is_free and cur_pointer.size >= p.need_mem:
            return (True, cur_pointer.allocate_mem(p.need_mem), cur_pointer.prev)# type: ignore
        cur_pointer = cur_pointer.next # type: ignore
    return (False, None, None) # type: ignore

def Best_fit(head:Memory, p:process) -> typing.Tuple[bool, Memory or None]:
    cur = head
    best_pair = (None, 99999)
    assert isinstance(cur, Memory)
    while(cur != None):
        if cur.is_free and cur.size >= p.need_mem:
            if cur.size - p.need_mem < best_pair[1]:
                best_pair = (cur.prev.next, cur.size - p.need_mem) # type: ignore
        cur = cur.next
    return (True, best_pair[0].allocate_mem(p.need_mem)) if best_pair[0] != None else (False, None) # type: ignore 

def Worst_fit(head:Memory, p:process) -> typing.Tuple[bool, Memory or None]:
    cur = head
    worst_pair = (None, -1)
    assert isinstance(cur, Memory)
    while(cur != None):
        if cur.is_free and cur.size >= p.need_mem:
            if cur.size - p.need_mem > worst_pair[1]:
                worst_pair = (cur.prev.next, cur.size - p.need_mem) # type: ignore
        cur = cur.next
    return (True, worst_pair[0].allocate_mem(p.need_mem)) if worst_pair[0] != None else (False, None) # type: ignore 

from Classes import Memory, process
import typing


def First_fit(head:Memory, p:process) -> typing.Tuple[bool, Memory or None]:
    cur = head.next
    assert isinstance(cur, Memory)
    while(cur != None):
        if cur.is_free and cur.size >= p.need_mem:
            return (True, cur.allocate_mem(p.need_mem))
        cur = cur.next
    return (False, None) # type: ignore
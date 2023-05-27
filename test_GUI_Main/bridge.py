from main import linked_list_init
import typing
from Algorithms import First_fit
from Classes import process, Memory

def allocate(size:int, name:str, algorithm:typing.Callable) -> typing.Tuple[bool, int | None]: # type: ignore
    if algorithm == 'First-fit':
        flag, Mem = First_fit(head, process(need = size))
        if flag:
            Mem_dict[name] = Mem
            return flag, Mem.begin
        else:
            return flag, None
    else:
        # todo 其它算法
        pass

def free(name:str) -> None:
    Mem_dict[name].free_mem()
    del Mem_dict[name]

head = linked_list_init()
Mem_dict:typing.Dict[str, Memory] = {}
from main import linked_list_init
import typing
from Algorithms import First_fit
from Classes import process, Memory

def allocate_memory(size:int, name:str, algorithm:str) -> typing.Tuple[bool, int or None]: # type: ignore
    if algorithm == 'First-fit':
        flag, Mem = First_fit(head, process(need = size))
        if flag:
            Mem_dict[name] = Mem
            return flag, Mem.begin
        else:
            return flag, None # type: ignore
    else:
        # todo 其它算法
        pass

def free_memory(name:str) -> None:
    Mem_dict[name].free_mem()
    del Mem_dict[name]

def main():
    global head
    global Mem_dict
    
    head = linked_list_init()
    # Mem_dict:typing.Dict[str, Memory] = {}
    Mem_dict = {}
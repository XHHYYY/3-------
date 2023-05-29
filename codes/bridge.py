import typing
from Algorithms import *
from Classes import process, linked_list_init

class bridge():
    def __init__(self) -> None:
        self.cur_pointer = None
        
    
    def allocate_memory(self, size:int, name:str, algorithm:str) -> typing.Tuple[bool, int or None]: # type: ignore
        if algorithm == 'First-fit':
            flag, Mem = First_fit(head, process(need = size))
            if flag:
                self.Mem_dict[name] = Mem
                return flag, Mem.begin
            else:
                return flag, None # type: ignore
        elif algorithm == 'Next-fit':
            if self.cur_pointer == None or self.cur_pointer.next == None:
                self.cur_pointer = head
            flag, Mem, self.cur_pointer = Next_fit(self.cur_pointer, process(need = size)) # type: ignore
            if flag:
                self.Mem_dict[name] = Mem
                return flag, Mem.begin
            else:
                self.cur_pointer = head
                flag, Mem, self.cur_pointer = Next_fit(self.cur_pointer, process(need = size)) # type: ignore
                if flag:
                    self.Mem_dict[name] = Mem
                return (flag, None) if not flag else (flag, Mem.begin) # type: ignore
        elif algorithm == 'Best-fit':
            flag, Mem = Best_fit(head, process(need = size))
            if flag:
                self.Mem_dict[name] = Mem
                return flag, Mem.begin
            else:
                return flag, None # type: ignore
        elif algorithm == 'Worst-fit':
            flag, Mem = Worst_fit(head, process(need = size))
            if flag:
                self.Mem_dict[name] = Mem
                return flag, Mem.begin
            else:
                return flag, None # type: ignore



    def free_memory(self, name:str) -> None:
        self.Mem_dict[name].free_mem()
        del self.Mem_dict[name]

    def main(self):
        global head
        
        head = linked_list_init()
        self.head = head

        self.Mem_dict = {}
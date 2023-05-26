

class Memory():
    def __init__(self, num=0, is_free=True, begin=0, size=1024, next=None) -> None:
        self.mem_num    = num
        self.is_free    = is_free
        self.begin      = begin
        self.size       = size
        self.next       = next
        
    def allocate_mem(self, size, prev_next):
        if size > self.size:
            raise Exception('Memory Overflow')
        elif size == self.size:
            self.is_free = False
            return self
        
        self.begin = self.begin + size
        self.size  = self.size - size
        self.update_num(True)
        
        new_mem = Memory(self.mem_num-1, False, self.begin, size, self)
        prev_next = new_mem
        new_mem.next = self
        
    def free_mem(self):
        if self.is_free:
            raise Exception('Memory already free')
        
        
    def update_num(self, is_allocate):
        if self.next != None:
            self.next.update_num()
        self.mem_num += 1 if is_allocate else -1
        
def read_sequence() -> list:
    with open('./codes/sequence.txt', 'r') as f:
        txt = f.read()
    requirement_list = []
    list_sequence = txt.split('\n')
    for requirement in list_sequence:
        if requirement == '':
            break
        temp = list(map(int, requirement.split()))
        requirement_list.append(temp)
    return requirement_list

if __name__ == '__main__':
    requirements = read_sequence()
    
class Memory():
    def __init__(self, num=0, is_free=True, begin=0, size=1024, next=None, prev=None) -> None:
        self.mem_num    = num
        self.is_free    = is_free
        self.begin      = begin
        self.size       = size
        self.next       = next
        self.prev       = prev
        
    def allocate_mem(self, size):
        # 输入检查
        if size > self.size:
            raise Exception('Memory Overflow')
        
        
        elif size == self.size:
            self.is_free = False
            return self
        
        # 申请新节点
        new_mem = Memory(self.mem_num, False, self.begin, size, self, self.prev)
        if self.prev != None:
            self.prev.next = new_mem
        
        self.prev = new_mem
        self.begin = self.begin + size
        self.size  = self.size - size
        # 更新后续节点的序号
        self.update_num(is_allocate=True)
        
        return new_mem
        
    def free_mem(self):
        # 输入检查
        if self.is_free:
            raise Exception('Memory already free')
        if self.prev == None:
            raise Exception('Free head Error')
        
        # 左右皆空
        if self.prev != None and self.next != None and self.prev.is_free and self.next.is_free:
            if self.next.next != None:
                self.next.next.update_num(is_allocate=False)
                self.next.next.update_num(is_allocate=False)
                self.next.next.prev = self.prev
            self.prev.next = self.next.next
            self.prev.size = self.prev.size + self.size + self.next.size
            del self.next
            temp = self.prev
            del self
            return temp
        # 左空
        elif self.prev.is_free:
            self.prev.size = self.prev.size + self.size
            self.prev.next = self.next
            if self.next != None:
                self.next.prev = self.prev
                self.next.update_num(is_allocate=False)
            temp = self.prev
            del self
            temp.is_free = True
            return temp
        # 右空
        elif self.next != None and self.next.is_free:
            self.next.update_num(is_allocate=False)
            self.size = self.size + self.next.size
            if self.next.next != None:
                self.next.next.prev = self
            temp = self.next
            self.next = self.next.next
            del temp
            self.is_free = True
            return self
        # 左右皆满（或无）
        else:
            self.is_free = True
            return self
        
    # 更新序号
    def update_num(self, is_allocate:bool):
        if self.next != None:
            self.next.update_num(is_allocate)
        self.mem_num += 1 if is_allocate else -1
        
        
        
class process():
    def __init__(self, need, num=None, arrive_time=None, require_time=None):
        self.num            = num
        self.need_mem       = need
        self.arrive_time    = arrive_time
        self.require_time   = require_time
        
    # 用于堆排序
    def __lt__(self, other):
        assert isinstance(other, process)
        return self.require_time < other.require_time # type:ignore
    
    
    
def linked_list_init() -> Memory:
    init = Memory()
    head = Memory(-1, False, -1, 0, init)
    init.prev = head
    del init
    return head
import heapq
import typing

class Memory():
    def __init__(self, num=0, is_free=True, begin=0, size=1024, next=None, prev=None) -> None:
        self.mem_num    = num
        self.is_free    = is_free
        self.begin      = begin
        self.size       = size
        self.next       = next
        self.prev       = prev
        print('init active')

    def __del__(self):
        print('del active, num = {}'.format(self.mem_num))
        
    def allocate_mem(self, size):
        if size > self.size:
            raise Exception('Memory Overflow')
        elif size == self.size:
            self.is_free = False
            return self
        
        
        new_mem = Memory(self.mem_num, False, self.begin, size, self, self.prev)
        if self.prev != None:
            self.prev.next = new_mem
        
        self.prev = new_mem
        self.begin = self.begin + size
        self.size  = self.size - size
        self.update_num(is_allocate=True)
        
        return new_mem
        
    def free_mem(self):
        if self.is_free:
            raise Exception('Memory already free')
        if self.prev == None:
            raise Exception('Free head Error')
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
        else:
            self.is_free = True

        
    def update_num(self, is_allocate:bool):
        if self.next != None:
            self.next.update_num(is_allocate)
        self.mem_num += 1 if is_allocate else -1
        
class process():
    def __init__(self, num, need, arrive_time, require_time):
        self.num            = num
        self.need_mem       = need
        self.arrive_time    = arrive_time
        self.require_time   = require_time
        
    # def __lt__(self, other):
    #     assert isinstance(other, process)
    #     return self.require_time < other.require_time

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

def CPU(head:Memory, requirements:typing.List[process], 
        algorithm:typing.Callable[[Memory, process], typing.Tuple[bool, Memory]]):
    time = 0
    waiting_list:list[process] = []
    occupation_heap:typing.List[typing.Tuple[int, process, Memory]] = []
    heapq.heapify(occupation_heap)
    
    while(requirements != []):
        time += 1
        # 检查进程队列此时是否需要进入WL
        while(requirements[0].arrive_time == time):
            waiting_list.append(requirements.pop(0))
        # 使占用中的进程需求时间-1
        for i, _ in enumerate(occupation_heap):
            temp = occupation_heap[i]
            occupation_heap[i] = (temp[0]-1, temp[1], temp[2])
            del temp
        # 释放到时间的进程
        if occupation_heap != []:
            while(heapq.nsmallest(1, occupation_heap)[0][0] == 0):
                temp = heapq.nsmallest(1, occupation_heap)[0][1]
                print(temp.num, temp.need_mem, temp.arrive_time, temp.require_time, 'deleted')
                # todo 图形化界面修改
                heapq.heappop(occupation_heap)[2].free_mem()
        ##### 从WL中尝试加入到时间的进程
        # 顺序搜索法，逐一加入
        # 已完成函数入口，下一步需要完成具体函数
        # 考虑返回值，若返回True说明加入成功，从WL中弹出，否则等待至下一周期
        try:
            while(1):
                flag, Mem = algorithm(head, waiting_list[0])
                if flag:
                    p_temp = waiting_list.pop(0)
                    heapq.heappush(occupation_heap, (p_temp.require_time, p_temp, Mem))
                    print(p_temp.num, p_temp.need_mem, p_temp.arrive_time, p_temp.require_time, 'added')
                    continue
                else:
                    break
        except:
            pass
        
def First_fit(head:Memory, p:process) -> typing.Tuple[bool, Memory or None]:
    cur = head.next
    assert isinstance(cur, Memory)
    while(cur != None):
        if cur.is_free and cur.size >= p.need_mem:
            return (True, cur.allocate_mem(p.need_mem))
        cur = cur.next
    return (False, None) # type: ignore



if __name__ == '__main__':
    requirements = read_sequence()
    init = Memory()
    head = Memory(-1, False, -1, 0, init)
    init.prev = head
    del init
    
    CPU(head, requirements, First_fit)
    
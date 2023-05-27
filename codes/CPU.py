import heapq
import typing
from Classes import Memory, process


def CPU(head:Memory, requirements:typing.List[process], 
        algorithm:typing.Callable[[Memory, process], typing.Tuple[bool, Memory]]):
    time = 0
    waiting_list:list[process] = []
    occupation_heap:typing.List[typing.Tuple[process, Memory]] = []
    heapq.heapify(occupation_heap)
    
    while(requirements != [] or waiting_list != [] or occupation_heap != []):
        time += 1
        # 检查进程队列此时是否需要进入WL
        try:
            while(requirements[0].arrive_time == time):
                waiting_list.append(requirements.pop(0))
        except IndexError:
            pass
        # 使占用中的进程需求时间-1
        for i, _ in enumerate(occupation_heap):
            occupation_heap[i][0].require_time -= 1
        # 释放到时间的进程
        try:
            while(heapq.nsmallest(1, occupation_heap)[0][0].require_time == 0):
                temp = heapq.nsmallest(1, occupation_heap)[0][0]
                print(temp.num, temp.need_mem, temp.arrive_time, temp.require_time, 'deleted, time =', time)
                # todo 图形化界面修改
                heapq.heappop(occupation_heap)[1].free_mem()
        except IndexError:
            pass
        ##### 从WL中尝试加入到时间的进程
        # 顺序搜索法，逐一加入
        # 已完成函数入口，下一步需要完成具体函数
        # 考虑返回值，若返回True说明加入成功，从WL中弹出，否则等待至下一周期
        try:
            while(1):
                flag, Mem = algorithm(head, waiting_list[0])
                if flag:
                    p_temp = waiting_list.pop(0)
                    heapq.heappush(occupation_heap, (p_temp, Mem))
                    print(p_temp.num, p_temp.need_mem, p_temp.arrive_time, p_temp.require_time, 'added, time =', time)
                    continue
                else:
                    break
        except IndexError:
            pass
        

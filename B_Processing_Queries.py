# from collections import deque

# def processing_queries(n: int, b: int, arrivals: list[int], dur: list[int]) -> list[int]:
#     q = deque()                # (duration, idx)
#     tail = 0
#     ans  = [-1]*n

#     for i in range(n):
#         t, d = arrivals[i], dur[i]

#         # Finish all jobs whose completion precedes the new arrival
#         while q and tail <= t:
#             td, j = q.popleft()
#             tail += td
#             ans[j] = tail

#         if tail <= t:          # server idle now
#             tail = t + d
#             ans[i] = tail
#         elif len(q) < b:       # enqueue
#             q.append((d, i))
#         else:                  # reject
#             ans[i] = -1

#     # drain remaining queue
#     while q:
#         td, j = q.popleft()
#         tail += td
#         ans[j] = tail
#     return ans
# import heapq
# from typing import List, Tuple

# def process_priority_queries(
#     queries: List[Tuple[int, int, int]],
#     queue_capacity: int
# ) -> List[int]:
#     """Process server queries with priority-based queue management."""
#     completion_times = [-1] * len(queries)
#     priority_queue = []
#     sequence_counter = 0
    
#     current_job_index = -1
#     current_job_end_time = 0
#     current_time = 0
    
#     durations = [duration for _, duration, _ in queries]
    
#     for query_index, (arrival_time, duration, priority) in enumerate(queries):
#         # Complete jobs that finish before current arrival
#         while (current_job_index != -1 and 
#                current_job_end_time <= arrival_time):
#             current_time = current_job_end_time
#             completion_times[current_job_index] = current_job_end_time
            
#             if priority_queue:
#                 # Start highest priority waiting job
#                 _, _, next_job_index = heapq.heappop(priority_queue)
#                 current_job_index = next_job_index
#                 current_job_end_time = current_time + durations[next_job_index]
#             else:
#                 # Server becomes idle
#                 current_job_index = -1
        
#         # Handle new query arrival
#         if current_job_index == -1:
#             # Server idle, start immediately
#             current_time = arrival_time
#             current_job_index = query_index
#             current_job_end_time = arrival_time + duration
#         elif len(priority_queue) < queue_capacity:
#             # Queue has space, add with priority
#             heapq.heappush(priority_queue, 
#                           (-priority, sequence_counter, query_index))
#             sequence_counter += 1
#         else:
#             # Queue full, reject query
#             completion_times[query_index] = -1
    
#     # Process remaining jobs after last arrival
#     while current_job_index != -1:
#         current_time = current_job_end_time
#         completion_times[current_job_index] = current_job_end_time
        
#         if priority_queue:
#             _, _, next_job_index = heapq.heappop(priority_queue)
#             current_job_index = next_job_index
#             current_job_end_time = current_time + durations[next_job_index]
#         else:
#             current_job_index = -1
    
#     return completion_times

# from collections import deque
# def process_queue(n, b, L, t, d):
#     ans = [-1] * n
#     Q   = deque()          # waiting indices, FIFO

#     run_id  = -1           # index of job currently executing
#     run_end = 0            # when that job will finish

#     def can_finish(j, start):          # helper uses closure vars
#         return start + d[j] <= t[j] + L[j]

#     for i in range(n):
#         # ---------- flush everything finishing before t[i] ----------
#         while run_id != -1 and run_end <= t[i]:
#             now          = run_end
#             ans[run_id]  = run_end
#             run_id       = -1          # CPU idle

#             # start first queue job that can still meet its deadline
#             while Q:
#                 j = Q.popleft()
#                 if can_finish(j, now):
#                     run_id  = j
#                     run_end = now + d[j]
#                     break
#                 else:                  # dropped due to missed deadline
#                     ans[j] = -1

#         # ---------- process new arrival i ----------
#         if run_id == -1:               # server idle
#             if can_finish(i, t[i]):
#                 run_id  = i
#                 run_end = t[i] + d[i]
#             else:
#                 ans[i] = -1            # impossible even if started now
#         else:                          # server busy
#             if len(Q) < b:
#                 Q.append(i)
#             else:
#                 ans[i] = -1            # queue full

#     # ---------- drain what is left ----------
#     while run_id != -1:
#         now         = run_end
#         ans[run_id] = run_end
#         run_id      = -1
#         while Q:
#             j = Q.popleft()
#             if can_finish(j, now):
#                 run_id  = j
#                 run_end = now + d[j]
#                 break
#             else:
#                 ans[j] = -1

#     # any jobs still waiting cannot ever run (deadline passed)
#     while Q:
#         ans[Q.popleft()] = -1
#     return ans

# n, b = (int(_) for _ in input().split())
# arrivals, dur, L =[], [], []
# for _ in range(n):
#     arr, d = (int(_) for _ in input().split())
#     arrivals.append(arr)
#     dur.append(d)
#     L.append(float('inf'))
    
# print(*process_queue(n, b, L, arrivals, dur))

import sys
from collections import deque

def batch_server(n, b, k, T, D):
    ans = [-1] * n
    Q   = deque()               # waiting indices
    free_at = 0                 # time when server becomes idle (0 == idle at start)

    def start_batch(now: int):
        """Pop ≤k jobs, set their finish times, and update free_at (closure)."""
        nonlocal free_at
        take = min(k, len(Q))
        max_d = 0
        for _ in range(take):
            j = Q.popleft()
            finish = now + D[j]
            ans[j] = finish
            if D[j] > max_d:
                max_d = D[j]
        free_at = now + max_d    # server busy until then

    for i in range(n):
        t_i, d_i = T[i], D[i]

        # 1) finish batches that end no later than arrival time t_i
        while free_at and free_at <= t_i:
            now = free_at
            if Q:
                start_batch(now)          # immediately start next batch
            else:                         # nothing waiting → idle until t_i
                free_at = 0
                break

        # 2) arrival handling
        if free_at == 0:                  # server idle
            Q.append(i)                   # queue was empty or not
            start_batch(t_i)              # new (or first) batch
        else:                             # server busy
            if len(Q) < b:
                Q.append(i)
            else:
                ans[i] = -1               # queue full → reject

    # 3) drain remaining jobs after last arrival
    now = free_at
    while free_at:                        # while server still busy
        while free_at and free_at == now: # batch just ended
            if Q:
                start_batch(now)
                now = free_at
            else:
                free_at = 0               # done
    return ans


# ------------- driver -------------
if __name__ == "__main__":
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        sys.exit()
    it = iter(data)
    n, b, k = next(it), next(it), 1
    T, D = [], []
    for _ in range(n):
        T.append(next(it))
        D.append(next(it))
    res = batch_server(n, b, k, T, D)
    print(*res)

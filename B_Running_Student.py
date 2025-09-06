# from math import *

# def solve(n, vb, vs, stops, xu, yu):
#     res = 1
#     delta_x, delta_y = (xu-stops[1]), yu
#     t_min = stops[1]/vb + sqrt(delta_x**2 + delta_y**2)/vs

#     for idx in range(1, n):
#         delta_x, delta_y = (xu-stops[idx]), yu
#         t = stops[idx]/vb + sqrt(delta_x**2 + delta_y**2)/vs
#         if t_min >= t:
#             t_min = t
#             res = idx

#     return res + 1
def choose_stop_bruteforce(n, vb, vs, xs, xu, yu):
    """
    xs: list of n integers (x1 < x2 < ... < xn), with xs[0] == 0
    Returns the 1-based index of the chosen stop.
    """
    import math
    EPS = 1e-9
    best_t = float('inf')
    best_d = float('inf')
    best_i = -1

    for i in range(1, n):  # i=1..n-1 => stops 2..n (1-based)
        x = xs[i]
        bus_t = x / vb
        dx = xu - x
        dy = yu
        run_d = math.hypot(dx, dy)
        t = bus_t + run_d / vs

        if t + EPS < best_t:
            best_t = t
            best_d = run_d
            best_i = i + 1  # convert to 1-based index
        elif abs(t - best_t) <= EPS:
            if run_d + EPS < best_d:
                best_d = run_d
                best_i = i + 1

    return best_i

n, vb, vs = (int(_) for _ in input().split())
stops = [int(_) for _ in input().split()]
xu, yu = (int(_) for _ in input().split())

print(choose_stop_bruteforce(n, vb, vs, stops, xu, yu))

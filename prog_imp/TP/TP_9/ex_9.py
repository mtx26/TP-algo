from displayCpu import CpuPlot
import sort
import umons_cpu
import random

def get_list(lenght):
    return list(range(1, lenght + 1))

def linear_search(list, x):
    i = 0
    while i < len(list):
        if list[i] == x:
            return i
        i += 1
    else:
        return


def use_script(list, x):
    a = umons_cpu.cpu_time(linear_search, list, x)
    b = umons_cpu.cpu_time(sort.dicho_search, list, x)
    return a, b

def script_efficiency(point):
    r_lin = []
    r_dic = []

    for n in point:
        # a, b = use_script(get_list(n), random.randint(0, n))
        a, b = use_script(get_list(n), 100000000000000000000000000000)
        print(a, b)
        r_lin.append(a)
        r_dic.append(b)

    return r_lin, r_dic


def dispay_graph(point):
    r_sel, r_ins = script_efficiency(point)
    
    afficheur = CpuPlot(point)

    # Add two sets of data points
    afficheur.prepare(r_sel, "Linéaire")
    afficheur.prepare(r_ins, "Dichotomique")

    # Display
    afficheur.draw()

dispay_graph(list(range(0, 250000, 10000)))



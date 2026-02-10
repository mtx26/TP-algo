from displayCpu import CpuPlot
import sort
import random
import umons_cpu
import ex_5

def gen_random_list(lenght):
    rep = list(range(1, lenght + 1))
    random.shuffle(rep)
    return rep



def use_script(list):
    a = umons_cpu.cpu_time(sort.selection_sort, list)
    b = umons_cpu.cpu_time(sort.insertion_sort, list)
    c = umons_cpu.cpu_time(sort.merge_sort, list)
    d = umons_cpu.cpu_time(ex_5.bubble_sort, list)
    e = umons_cpu.cpu_time(sort.python_sort, list)
    return a, b, c, d, e


def script_efficiency(point):
    r_sel = []
    r_ins = []
    r_fus = []
    r_bub = []
    r_pyt = []

    for n in point:
        a, b, c, d, e = use_script(gen_random_list(n))
        print(a, b, c, d, e)
        r_sel.append(a)
        r_ins.append(b)
        r_fus.append(c)
        r_bub.append(d)
        r_pyt.append(e)

    return r_sel, r_ins, r_fus, r_bub, r_pyt

def dispay_graph(point):
    r_sel, r_ins, r_fus, r_bub, r_pyt = script_efficiency(point)
    
    afficheur = CpuPlot(point)

    # Add two sets of data points
    afficheur.prepare(r_sel, "Selection")
    afficheur.prepare(r_ins, "Insertion")
    afficheur.prepare(r_fus, "Fusion")
    afficheur.prepare(r_bub, "Bulle")
    afficheur.prepare(r_pyt, "Python sort")

    # Display
    afficheur.draw()

dispay_graph(list(range(0, 10000, 100)))








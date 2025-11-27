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
    print(list)
    a = umons_cpu.cpu_time(sort.selection_sort, list)
    b = umons_cpu.cpu_time(sort.insertion_sort, list)
    c = umons_cpu.cpu_time(sort.merge_sort, list)
    d = umons_cpu.cpu_time(ex_5.bubble_sort, list)
    return a, b, c, d


def script_efficiency(point):
    r_sel = []
    r_ins = []
    r_fus = []
    r_bub = []

    for n in point:
        a, b, c, d = use_script(gen_random_list(n))
        print(a, b, c, d)
        r_sel.append(a)
        r_ins.append(b)
        r_fus.append(c)
        r_bub.append(d)

    return r_sel, r_ins, r_fus, r_bub

def dispay_graph(point):
    r_sel, r_ins, r_fus, r_bub = script_efficiency(point)
    
    afficheur = CpuPlot(point)

    # Add two sets of data points
    afficheur.prepare(r_sel, "Selection")
    afficheur.prepare(r_ins, "Insertion")
    afficheur.prepare(r_fus, "Fusion")
    afficheur.prepare(r_bub, "Bulle")

    # Display
    afficheur.draw()

dispay_graph(list(range(0, 1000, 10)))








import sys
from graph_utils import create_network_graph
from compare import get_run_result
import numpy as np
from result_utils import save_data


def graphViNE_run(physical_graph, requests, save=True, load=2000, max_time=500):
    physical_graph_vine = physical_graph.copy()
    request_graphs_graph_vine = [r.copy() for r in requests]
    results = get_run_result(
        physical_graph_vine, request_graphs_graph_vine, method="graphViNE", traffic_load=load, max_time=max_time, cost_revenue=True, utils=True)

    if save:
        names = ['gv_probs', 'gv_blockeds', 'gv_num', 'gv_cost',
                 'gv_revenue', 'gv_cpu_utils', 'gv_link_utils']
        for i in range(len(results)):
            save_data(results[i], names[i])
    [gv_probs, gv_blockeds, gv_num, gv_cost, gv_revenue,
        gv_cpu_utils, gv_link_utils] = results
    return gv_probs, gv_blockeds, gv_num, gv_cost, gv_revenue, gv_cpu_utils, gv_link_utils


def neuroViNE_run(physical_graph, requests, save=True, load=2000, max_time=500):
    physical_neuro = physical_graph.copy()
    request_graphs_neuro = [r.copy() for r in requests]
    results = get_run_result(
        physical_neuro, request_graphs_neuro, method="neuroViNE", traffic_load=load, max_time=max_time, cost_revenue=True, utils=True)

    if save:
        names = ['nv_probs', 'nv_blockeds', 'nv_num', 'nv_cost',
                 'nv_revenue', 'nv_cpu_utils', 'nv_link_utils']
        for i in range(len(results)):
            save_data(results[i], names[i])
    [nv_probs, nv_blockeds, nv_num, nv_cost, nv_revenue,
        nv_cpu_utils, nv_link_utils] = results
    return nv_probs, nv_blockeds, nv_num, nv_cost, nv_revenue, nv_cpu_utils, nv_link_utils


def grc_run(physical_graph, requests, save=True, load=2000, max_time=500):
    physical_grc = physical_graph.copy()
    request_graphs_grc = [r.copy() for r in requests]
    results = get_run_result(
        physical_grc, request_graphs_grc, method="grc", traffic_load=load, max_time=max_time, cost_revenue=True, utils=True)

    if save:
        names = ['grc_probs', 'grc_blockeds', 'grc_num', 'grc_cost',
                 'grc_revenue', 'grc_cpu_utils', 'grc_link_utils']
        for i in range(len(results)):
            save_data(results[i], names[i])
    [grc_probs, grc_blockeds, grc_num, grc_cost,
        grc_revenue, grc_cpu_utils, grc_link_utils] = results
    return grc_probs, grc_blockeds, grc_num, grc_cost, grc_revenue, grc_cpu_utils, grc_link_utils


def best_fit_run(physical_graph, requests, save=True, load=2000, max_time=500):
    physical_best_fit = physical_graph.copy()
    request_graphs_best_fit = [r.copy() for r in requests]
    results = get_run_result(
        physical_best_fit, request_graphs_best_fit, method="bestFit", traffic_load=load, max_time=max_time, cost_revenue=True, utils=True)

    if save:
        names = ['bf_probs', 'bf_blockeds', 'bf_num', 'bf_cost',
                 'bf_revenue', 'bf_cpu_utils', 'bf_link_utils']
        for i in range(len(results)):
            save_data(results[i], names[i])
    [bf_probs, bf_blockeds, bf_num, bf_cost, bf_revenue,
        bf_cpu_utils, bf_link_utils] = results
    return bf_probs, bf_blockeds, bf_num, bf_cost, bf_revenue, bf_cpu_utils, bf_link_utils


def first_fit_run(physical_graph, requests, save=True, load=2000, max_time=500):
    physical_first_fit = physical_graph.copy()
    request_graphs_first_fit = [r.copy() for r in requests]
    results = get_run_result(
        physical_first_fit, request_graphs_first_fit, method="firstFit", traffic_load=load, max_time=max_time, cost_revenue=True, utils=True)

    if save:
        names = ['ff_probs', 'ff_blockeds', 'ff_num', 'ff_cost',
                 'ff_revenue', 'ff_cpu_utils', 'ff_link_utils']
        for i in range(len(results)):
            save_data(results[i], names[i])
    [ff_probs, ff_blockeds, ff_num, ff_cost, ff_revenue,
        ff_cpu_utils, ff_link_utils] = results
    return ff_probs, ff_blockeds, ff_num, ff_cost, ff_revenue, ff_cpu_utils, ff_link_utils


def compute():
    np.random.seed(64)  # to get a unique result every time
    physical_graph = create_network_graph(nodes_num=100)
    requests = [create_network_graph(np.random.randint(3, 11), min_feature_val=4, max_feature_val=10,
                                     min_link_val=4, max_link_val=10, connection_prob=0.7, life_time=(100, 900)) for i in range(8300)]

    load = 1000
    max_time = 2000
    # graphViNE_run(physical_graph, requests, load=load, max_time=max_time)
    # neuroViNE_run(physical_graph, requests, load=load, max_time=max_time)
    # grc_run(physical_graph, requests, load=load, max_time=max_time)
    # best_fit_run(physical_graph, requests, load=load, max_time=max_time)
    first_fit_run(physical_graph, requests, load=load, max_time=max_time)


def compare():
    grc_probs = np.fromfile('./results/Load1000/grc_probs.dat')
    nv_probs = np.fromfile('./results/Load1000/nv_probs.dat')
    gv_probs = np.fromfile('./results/Load1000/gv_probs.dat')
    bf_probs = np.fromfile('./results/Load1000/bf_probs.dat')
    ff_probs = np.fromfile('./results/ff_probs.dat')

    from result_utils import draw_blocking_prob
    draw_blocking_prob([grc_probs, gv_probs, bf_probs, ff_probs, nv_probs],
                       ['GRC', 'GraphViNE', 'Best Fit', 'First Fit', 'NeuroViNE'],
                       ['r', 'b', 'purple', 'green', 'y'],
                       'Time Units', 'Blocking prob', 'Models Block Probability')
    


commands = ['--help', '-h', '--get_results', '--compare_results']
help = '''
    Oprtions:
        --help / -h : shows this help!
        --get_resutls : computes results of models and store in ./results repo.
        --compare_resutls : compares results using matplotlib
        '''
if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in commands:
        print('Undefiend Options')
        print(help)
    elif sys.argv[1] == commands[0] or sys.argv[1] == commands[1]:
        print(help)
    elif sys.argv[1] == commands[2]:
        compute()
    elif sys.argv[1] == commands[3]:
        compare()

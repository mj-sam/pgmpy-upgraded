def Accuracy(optimal,estimated):
    """
    Parameter :
        optimal :
            the optimal learned graph object
        estimated :
            the estimated learned graph object
    """
    opt_edges = set(optimal.edges())
    est_edges = set(estimated.edges())
    TP = len(opt_edges.intersection(est_edges))
    FP = len(est_edges.difference(opt_edges))
    FN = len(opt_edges.difference(est_edges))
    Var = int(optimal.size())
    complete_graph_edge_count = (Var * Var -1) / 2
    TN = complete_graph_edge_count - (TP + FP + FN )
    
    accuracy = (float(TP) + float(TN)) / (float(TP) + float(TN) + float(FP) + float(FN))

    """
    References
    ---------
    [1] Liu, Z., Malone, B. and Yuan, C., 2012. Empirical evaluation of scoring functions for Bayesian
        network model selection. BMC bioinformatics, 13(15), p.S14.
    """
    
    return accuracy

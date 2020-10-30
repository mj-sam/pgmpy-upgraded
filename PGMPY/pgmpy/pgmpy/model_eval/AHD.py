def AHD(optimal,estimated):
    """
    Parameter :
        optimal :
            the optimal learned graph object
        estimated :
            the estimated learned graph object
    """
    opt_edges = set(optimal.edges())
    est_edges = set(estimated.edges())
    FP = len(est_edges.difference(opt_edges))
    FN = len(opt_edges.difference(est_edges))
    AHD = (float(FP) + float(FN)) / optimal.order()
    
    """
    References
    ---------
    [1] Liu, Z., Malone, B. and Yuan, C., 2012. Empirical evaluation of scoring functions for Bayesian
        network model selection. BMC bioinformatics, 13(15), p.S14.
    """
    return AHD
    

def SHD(optimal,estimated):
    """
    Parameter :
        optimal :
            the optimal learned graph object
        estimated :
            the estimated learned graph object
    """
    opt_edges = set(optimal.edges())
    est_edges = set(estimated.edges())
    opt_not_est = opt_edges.difference(est_edges)
    est_not_opt = est_edges.difference(opt_edges)
    c = 0;
    for p1 in opt_not_est:
        for p2 in est_not_opt:
            if(set(p1) == set(p2)):
                c +=1
    SHD_score = len(opt_not_est) + len(est_not_opt) - c
    
    """
    References
    ---------
    [1] de Jongh, M. and Druzdzel, M.J., 2009. A comparison of structural distance
        measures for causal Bayesian network models. Recent Advances in Intelligent 
        Information Systems,Challenging Problems of Science, Computer Science series, 
        pp.443-456.
    """
    return SHD_score

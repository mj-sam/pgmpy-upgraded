from math import log

from pgmpy.estimators import StructureScore
class FNMLScore(StructureScore):
    def __init__(self, data):
        """
        Parameters
        ----------
        data: pandas DataFrame object
        """
        super(FNMLScore, self).__init__(data)

    def local_score(self, variable, parents):
        
        var_states = self.state_names[variable]
        var_cardinality = len(var_states)
        state_counts = self.state_counts(variable, parents)
        sample_size = len(self.data)
        num_parents_states = float(len(state_counts.columns))
        score = 0
        
        for parents_state in state_counts:
            conditional_sample_size = sum(state_counts[parents_state])
            for state in var_states:
                if state_counts[parents_state][state] > 0:
                    #print state_counts[parents_state][state]
                    score += state_counts[parents_state][state] * (log(state_counts[parents_state][state]) -
                                                                   log(conditional_sample_size))
                # same as we calculate AIC 
                # but we subtract penalty here for each factor
            if conditional_sample_size > 0:
                score -= 0.5 * (log(conditional_sample_size)) * float(len(state_counts))
                #print score
                
        """
        References
        ---------
        [1] Kontkanen, P. and Myllymki, P., 2007. A linear-time algorithm for computing
            the multinomial stochastic complexity.
            Information Processing Letters, 103(6), pp.227-233.
        
        """
        return score

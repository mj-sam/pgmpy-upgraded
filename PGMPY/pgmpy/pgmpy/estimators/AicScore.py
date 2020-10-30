from math import log

from pgmpy.estimators import StructureScore


class AicScore(StructureScore):
    def __init__(self, data):
        """
        Parameters
        ----------
        data: pandas DataFrame object
        """
        super(AicScore, self).__init__(data)

    def local_score(self, variable, parents):
        
        var_states = self.state_names[variable]
        var_cardinality = len(var_states)
        state_counts = self.state_counts(variable, parents)
        sample_size = len(self.data)
        num_parents_states = float(len(state_counts.columns))
        score = 0
        
        for parents_state in state_counts:
            # for each state of parents of given variable
            conditional_sample_size = sum(state_counts[parents_state])
            # how many sample have this parents state
            for state in var_states:
                # for each state of given variable
                if state_counts[parents_state][state] > 0:
                    #if we have sample with this condition we compute the likelyhood
                    score += state_counts[parents_state][state] * (log(state_counts[parents_state][state]) -
                                                                   log(conditional_sample_size))

        # the score is just a Likelyhood till here but for 
        #avoid over fitting we add the penalty below
        B = num_parents_states * (var_cardinality - 1)
        score -= B
        """
        References
        ---------
        [1] Koller & Friedman, Probabilistic Graphical Models - Principles and Techniques, 2009
        Section 18.3.4-18.3.6 (esp. page 806)
        """
        return score


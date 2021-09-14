test_value = 0.915

def complement(p):
    if(p <= 1):
        c = 1-p
        return c
    else:
        return 'Invalid p_A'


#-- correct code --#
def joint(p_a, p_b):
    j = p_a*p_b
    return j

#-- correct code --#
def total_probability(p_d, p_p_d, p_n_d):
    total = p_d*p_p_d + (1-p_d)*p_n_d
    return total


#-- correct code --#
def bayes(p0, p1, p2):
    b = (p0 * p1)/(p0 * p1 + (1-p0) * (1-p2))
    return b
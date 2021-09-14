import matplotlib.pyplot as plt
import numpy as np

def distribution(sample_distribution, trials, num_bins):

    # array from 1 to sample_distribution
    pers = np.arange(1,sample_distribution + 1,1)
    
    # calculate array of relative probabilities for each sample
    lower = int(.35*len(pers))
    middle = int(.2*len(pers))
    upper = int(.40*len(pers))
    extreme = len(pers) - (lower + middle + upper)
    
    prob = [1.0]*(lower) + [.5]*middle + [2.0]*upper + [.5]*extreme
    
    # normalize probability distribution
    prob /= np.sum(prob)

    # take a random sample for number of times in trials variable
    probability_distribution = np.random.choice(pers, trials, p=prob)
    
    # return random sample size of trials variable
    return probability_distribution

def histogram_visualization(probability_distribution):
    plt.hist(probability_distribution, bins = 50)
    plt.title('Histogram of the Population')
    plt.xlabel('Value from the Population')
    plt.ylabel('Count')
    plt.xticks(np.linspace(0,50,11))
    plt.show()

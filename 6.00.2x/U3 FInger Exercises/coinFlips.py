import random
import matplotlib.pyplot as plt

def flip(num_flips):
    H = 0
    T = 0
    for flip_count in range(num_flips):
        result = random.choice(['H', 'T'])
        if result == 'H':
            H = H + 1
        else:
            T = T + 1
    return H/num_flips

def simFlips(num_flips, numTrials):
    mean = []
    for trial in range(numTrials):
        mean.append(flip(num_flips))
    return f'Mean = {sum(mean)/numTrials}'

def regress_to_mean(num_flips, numTrials):
    #Get fraction of heads for each trial of num_flips
    frac_heads = []
    for t in range(numTrials):
        frac_heads.append(flip(num_flips))
    #Find trials with extreme results and for each the next trial
    extremes, next_trials = [], []
    for i in range(len(frac_heads) - 1):
        if frac_heads[i] < 0.33 or frac_heads[i] > 0.66:
            extremes.append(frac_heads[i])
            next_trials.append(frac_heads[i+1])
    #Plot results
    plt.plot(range(len(extremes)), extremes, 'ko', label = 'Extreme')
    plt.plot(range(len(next_trials)), next_trials, 'k^',
                label = 'Next Trial')
    plt.axhline(0.5)
    plt.ylim(0, 1)
    plt.xlim(-1, len(extremes) + 1)
    plt.xlabel('Extreme Example and Next Trial')
    plt.ylabel('Fraction Heads')
    plt.title('Regression to the Mean')
    plt.legend(loc = 'best')
    plt.show()

def flip_plot(min_exp, max_exp):
    """Assume min_exp and max_exp positive ints, min_exp < max_exp
        Plot results of 2**min_exp to 2**max_exp coin flips"""
    ratios, diffs, xAxis = [], [], []
    for exp in range(min_exp, max_exp + 1):
        xAxis.append(2**exp)
    for num_flips in xAxis:
        num_heads = 0
        for n in range(num_flips):
            if random.choice(('H', 'T')) == 'H':
                num_heads = num_heads + 1
        num_tails = num_flips - num_heads
        try:
            ratios.append(num_heads/num_tails)
            diffs.append(abs(num_heads - num_tails))
        except ZeroDivisionError:
            continue
    plt.title('Difference Between Heads and Tails')
    plt.xlabel('Number of Flips')
    plt.ylabel('Abs(#Heads - #Tails)')
    plt.xticks(rotation = 'vertical')
    plt.plot(xAxis, diffs, 'k')
    plt.figure()
    plt.title('Heads/Tails Ratios')
    plt.xlabel('Number of Flips')
    plt.ylabel('#Heads/#Tails')
    plt.xticks(rotation = 'vertical')
    plt.plot(xAxis, ratios, 'k')
    plt.show()


# random.seed(0)
# regress_to_mean(15, 50)
flip_plot(4, 20)

import matplotlib.pyplot as plt
import numpy as np

def dice():
    return np.random.uniform() > 0.5

def f(x):
    for i in range(len(x)):
        x[i] = x[i]+1 if dice() else x[i]-1
    return x

# According to the recorder to plot the graph
def back_to_zero_count(records, dim:int, walks:int, steps:int):
    count = [len(r["back_to_zero"]) for r in records]
    ## Probability Density Function
    plt.hist(count, bins=100, density=True, alpha=0.8, color='g')
    plt.xlabel('Times')
    plt.ylabel('Probability')
    plt.title('Probability Density Function (Back to Origin)')
    plt.savefig(f"dim-{dim}_walks-{walks}_steps-{steps}_origin.png")
    plt.show()
    return None

def distance_plot(records, tpe:str, dim:int, walks:int, steps:int):
    last_x_dist = []
    for record in records:
        if tpe == "l1":
            last_x_dist.append(np.linalg.norm(record["last_x"], ord=1))
        elif tpe == "l2":
            last_x_dist.append(np.linalg.norm(record["last_x"], ord=2))
        else:
            raise ValueError("Invalid type")
    
    ## Probability Density Function
    plt.hist(last_x_dist, bins=100, density=True, rwidth=0.5, alpha=0.6, color='g')
    plt.xlabel('Distance')
    plt.ylabel('Probability')   
    plt.title(f'Probability Density Function ({tpe})')
    plt.savefig(f"dim-{dim}_walks-{walks}_steps-{steps}_{tpe}.png")
    plt.show()
    
    return None


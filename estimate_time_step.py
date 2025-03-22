import matplotlib.pyplot as plt
import seaborn as sns
import json, argparse
from tqdm import tqdm

def load_jsonl(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return [json.loads(l) for l in tqdm(lines, desc='Loading data', total=len(lines))]
    
def plot_time_step_distribution(time_step, dim, walks):
    plt.figure(figsize=(10, 5))
    sns.histplot(time_step, bins=100, linewidth=0.7, color='royalblue', stat='density')
    plt.title(f"Time step distribution for dim-{dim} walks-{walks}")
    plt.xlabel("Time step")
    plt.ylabel("Probability density")

    plt.savefig(f"dim-{dim}_walks-{walks}_time_step_distribution.png")
    plt.show()

def main(args):
    dim = args.dim
    walks = args.walks
    predir = args.predir

    pth = f'{predir}/dim-{dim}_walks-{walks}.jsonl'
    data = load_jsonl(pth)

    time_step = []
    for d in tqdm(data, desc='Estimating time step distribution', total=len(data)):
        st = 0
        for t in d["back_to_zero"]:
            time_step.append(t - st)
            st = t
        if(st < len(data)):
            time_step.append(1000 - st) # max time step is 1000 for all walks

    plot_time_step_distribution(time_step, dim, walks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Estimate time step distribution')
    parser.add_argument('--dim', type=int, default=2, help='Dimension of the walk') 
    parser.add_argument('--walks', type=int, default=1000000, help='Number of walks')
    parser.add_argument('--predir', type=str, default='statistics_jsonl', help='Directory of the data')
    args = parser.parse_args()

    main(args)
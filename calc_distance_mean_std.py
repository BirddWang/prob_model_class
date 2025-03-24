import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
from tqdm import tqdm


def load_jsonl(pth:str):
    print(f"Loading from {pth}...")
    with open(pth, 'r') as f:
        lines = f.readlines()
    return [json.loads(l) for l in tqdm(lines, desc='Loading jsonl')]

def calc_mean_std(data):
    mean = np.mean(data)
    std = np.std(data)
    return mean, std

def main():
    dimen = [1, 2, 3, 4]
    n_steps = [1e2, 1e3, 1e4, 1e5, 1e6]

    ## test
    dimen = [4]
    n_steps = [1e6]

    for d in dimen:
        for n in n_steps:
            data = load_jsonl(f'statistics_jsonl/dim-{d}_walks-{int(n)}.jsonl')
            data = [d['last_x'] for d in data]
            data = np.array(data)
            dist = np.linalg.norm(data, ord=2, axis=1)
            mean, std = calc_mean_std(dist)
            print(f"dim-{d}_steps-{int(n)}: mean={mean}, std={std}")
    return

if __name__ == "__main__":
    main()
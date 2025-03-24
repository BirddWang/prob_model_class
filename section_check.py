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


def main():
    dimen = [1, 2, 3, 4]
    sns.set_theme(palette='deep', font_scale=1)
    fig, ax = plt.subplots(2, 2, figsize=(20, 20))

    for dim in dimen:
        data = load_jsonl(f'statistics_jsonl/dim-{dim}_walks-10000.jsonl')
        print(len(data))

        # Count the number of times each section appears
        counts = {}
        for d in data:
            for s in d['section']:
                if s in counts:
                    counts[s] += 1
                else:
                    counts[s] = 1
            
        # Sort by section
        counts = dict(sorted(counts.items(), key=lambda item: item[0]))

        # Plot
        ax[(dim-1)//2][(dim-1)%2].bar(counts.keys(), counts.values(), color='b')
        ax[(dim-1)//2][(dim-1)%2].set_title(f"Dimension {dim}")
        ax[(dim-1)//2][(dim-1)%2].set_ylabel('Count')
        ax[(dim-1)//2][(dim-1)%2].grid(True)

    plt.savefig('section_check.png')
    plt.show()
    

if __name__ == '__main__':
    main()

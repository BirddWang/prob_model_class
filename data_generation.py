import numpy as np
import multiprocessing as mp
import json, argparse

from utils import f, back_to_zero_count, distance_plot
from section_finder import select_fn

def record(x, fn):
    section = fn(x)
    return {
        "section": int(section),
        "is_zero": np.all(x == 0),
    }

def test(d:int, steps:int, fn):
    recorder = {
        "back_to_zero": [],
        "section": []
    }
    x = np.zeros(int(d))
    # REPEAT
    for step in range(int(steps)):
        x = f(x)
        rec = record(x, fn)
        if rec["is_zero"]:
            recorder["back_to_zero"].append(step+1)
        recorder["section"].append(rec["section"])
    recorder["last_x"] = x
    return recorder

def worker_task(args):
    return test(*args)

## Main Test
def main(args):
    d = args.dimension
    walk_count = args.walks

    fn = select_fn(d)
    ## Parallel Computing
    num_workers = mp.cpu_count()
    with mp.Pool(num_workers) as pool:
        records = []
        for res in pool.imap_unordered(worker_task, [(d, args.steps, fn) for _ in range(walk_count)]):
            records.append(res)
    ## Plot
    distance_plot(records, "l1", d, walk_count)
    distance_plot(records, "l2", d, walk_count)
    back_to_zero_count(records, d, walk_count)
    ## Save the records
    with open(f"dim-{d}_walks-{walk_count}.jsonl", "w") as f:
        for record in records:
            record["last_x"] = record["last_x"].tolist()
            f.write(json.dumps(record) + "\n")
    return None

## Params
# Dimension = [1, 2, 3, 4]
# steps = 1000
# walks = [10**2, 10**3, 10**4, 10**5, 10**6]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Random Walk Simulation')
    parser.add_argument('--dimension', type=int, default=1, help='Dimension of the walk')
    parser.add_argument('--steps', type=int, default=1000, help='Number of steps')
    parser.add_argument('--walks', type=int, default=1000, help='Number of walks')
    args = parser.parse_args()
    
    main(args)
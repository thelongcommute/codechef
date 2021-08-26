# codechef.com/problems/TREEROOT

# RESULT: Produces correct answer but out of memory/out of time on codechef

import math
import itertools


def possible_children(n, parent, id_set):
    output = []
    for i in range(math.ceil(n / 2)):
        j = n - i
        if (i == 0 or i in id_set) and (j in id_set) and not ((i or j) == parent):
            output.append((i, j))
    if output:
        return output
    return [(0, 0)]


def possible_root(comb):
    children = {i for sub in comb.values() for i in sub}
    parents = set(comb.keys())
    return parents - children


T = int(input())
for _ in range(T):
    N = int(input())
    ids_sums = {}
    for _ in range(N):
        tmp = [int(x) for x in input().split(" ")]
        ids_sums[tmp[0]] = tmp[1]

    for i in ids_sums:
        ids_sums[i] = possible_children(ids_sums[i], i, ids_sums.keys())

ids = ids_sums.keys()

keys, values = zip(*ids_sums.items())
possible_combs = [dict(zip(keys, v)) for v in itertools.product(*values)]

# have to iterate over a copy of list because deleting items
for comb in possible_combs.copy():
    child1, child2 = zip(*comb.values())
    referenced_ids = list(child1 + child2)
    referenced_ids = [x for x in referenced_ids if x != 0]
    referenced_ids_set = set(referenced_ids)
    # drop any combinations that have a duplicate id
    if len(referenced_ids_set) != len(referenced_ids):
        possible_combs.remove(comb)

roots = set()
for comb in possible_combs:
    root = possible_root(comb)
    if root and root not in roots and len(root) == 1:
        roots.add(root.pop())

for root in roots:
    print(root)

import numpy as np, functools as ft
pairs =  [list(map(eval,l.split('\n'))) for l in open('input').read().rstrip().split('\n\n')]

def compare_values(left, right):
    match left, right:
        case int(), int(): return (left < right) - (right < left)
        case int(), list(): return compare_values([left], right)
        case list(), int(): return compare_values(left, [right])
        case list(), list():
            for i in [compare_values(i,j) for i,j in zip(left,right) if compare_values(i,j)!=0]:
                return i
            return compare_values(len(left), len(right))

corrects = [p+1 for p in range(len(pairs)) if  compare_values(pairs[p][0],pairs[p][1]) == 1]
ranked = sorted(sum(pairs,[]) + [[[2]], [[6]]] , key = ft.cmp_to_key(compare_values))[::-1]

print(sum(corrects), np.prod([ranked.index(d) +1 for d in [[[2]], [[6]]]]))

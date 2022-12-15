import re
import time
start = time.time()
input =  [list(map(int,re.findall(r'-?\d+', l))) for l in open('input').read().rstrip().split('\n')]

excluded, target, search, p2 = set(),2000000, 4000000, 0
for xs, ys, xb, yb in input:
    dist = abs(xs-xb)  + abs(ys-yb)
    ns = set()
    i = target - ys
    ns.update(set(zip(range(xs+ -(abs(dist) -abs(i)), xs + (abs(dist) -abs(i))+1), [ys+i]*(2*(abs(dist) -abs(i))+1)) ))
    ns = ns - set([(xb,yb)])
    excluded.update(ns)
p1 = time.time()
for xs, ys, xb, yb in input:
    dist = abs(xs-xb)  + abs(ys-yb)
    check = list(zip(range(xs+dist+1,xs,-1),range(ys,ys+dist+1,1)))
    check += list(zip(range(xs,xs-dist-1,-1),range(ys+dist+1,ys,-1)))
    check += list(zip(range(xs-dist-1,xs,1),range(ys,ys-dist-1,-1)))
    check += list(zip(range(xs,xs+dist+1,1),range(ys-dist-1,ys,1)))
    check = [c for c in check if 0 <= c[0] <= search and 0 <= c[1] <= search]

    for c in check:
        for xs, ys, xb, yb in input:
            dist = abs(xs-xb)  + abs(ys-yb)
            if abs(c[0]-xs) + abs(c[1] - ys) <= dist:
                break
        else:
            p2 = search * c[0] + c[1]
    if p2 > 0: break
print(len([x for x in excluded if x[1] == target]), p2)
print(f'p1: {p1 - start } seconds, total: {time.time() - start} seconds')

import numpy as np, copy
grid =  np.array([list(map(lambda x : ord(x) - 96, line)) for line in open('input').read().rstrip().split('\n')])
scores = np.full(grid.shape, np.inf)

target = np.where(grid == np.min(grid))
start = tuple(zip(*np.where(grid == -13)))[0]
grid[start], grid[target]  = 1, 26

dirs = [(0,1),(0,-1),(1,0),(-1,0)]
nns= lambda y,x : [(y+dy,x+dx) for dy,dx in dirs if  -1 < y+dy < len(grid) and -1<x+dx < len(grid[0])]

def path(grid, scores, start):
    if grid[start] != 1: return np.inf
    unvisited, visited, scores[start] = [start], set([start]), 1
    while len(unvisited) > 0:
        current = unvisited[np.argmin(grid[np.array(unvisited)[:,0],np.array(unvisited)[:,1]])]
        visited.add(current)
        unvisited.remove(current)

        for n in nns(*current):
            if n not in visited and n not in unvisited and grid[n] - grid[current] <=1:
                unvisited.append(n)
            if grid[n] - grid[current] <=1 and scores[current] + 1 < scores[n]:
                scores[n] = scores[current] + 1
    return scores[target] - 1

all = [path(copy.deepcopy(grid), copy.deepcopy(scores), s) for s in np.ndindex(grid.shape)]
print(path(copy.deepcopy(grid), copy.deepcopy(scores), start),  min(all))

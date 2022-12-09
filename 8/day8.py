import numpy as np
grid =  np.array([list(map(int,list(lines))) for lines in open('input').read().rstrip().split('\n')])
vis, dist = np.zeros_like(grid), np.pad(np.full(grid.shape,1),1,'constant', constant_values=-1)

for x,g in np.ndindex(grid.shape):
    hlines = min(map(max,[grid[x,:g], grid[x,g+1:], grid[:x,g],grid[x+1:,g]])) if x and g and x!= len(grid)-1 and g != len(grid)-1 else -1
    vis[x,g] = grid[x,g] > hlines
    for dir in [(1,0),(-1,0),(0,1),(0,-1)]:
        ix, iy, score = x, g, 0
        while dist[ix+1 + dir[0], iy+1+dir[1]] != -1 and grid[ix + dir[0], iy+dir[1]] < grid[x,g]:
            score +=1
            ix, iy = ix + dir[0], iy + dir[1]

        if dist[ix+1 + dir[0], iy+1+dir[1]] != -1:
            score += 1
        dist[x+1,g+1] = score * dist[x+1,g+1]

print(np.count_nonzero(vis > 0), np.max(dist))

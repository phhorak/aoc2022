import numpy as np
input = [list(map(lambda x:  eval('np.array((' + x + '))'), l.split(' -> '))) for l in open('input').read().rstrip().split('\n')]
max_x, max_y = max(sum([[x for x,_ in z] for z in input], [])), max(sum([[y for _,y in z] for z in input], []))
grid = np.zeros([max_x+1000, max_y+3])
grid[:,max_y+2] = -1

for l in input:
    for p in range(len(l)-1):
        dir = l[p+1] - l[p]
        for _ in range(np.max((np.abs(dir)))):
            grid[*l[p]] = -1
            l[p] += np.sign(dir)
        grid[*l[p]] = -1

def drop_sand(grid, c):
    parts = 0
    while grid[*(c + dirs['d'])] == 0 or grid[*(c + dirs['dl'])] == 0 or grid[*(c + dirs['dr'])] == 0  :
        for k in dirs.keys():
            if grid[*(c + dirs[k])] == 0:
                c += dirs[k ]
                break
        for k in dirs.keys():
            if (c + dirs[k])[1] > len(grid[0])-3:
                p1 = -1

    grid[*c] = 1
    return 1, p1


dirs = {'d': (0,1), 'dr': (-1,1), 'dl': (1,1)}


count, x, sols  = 0, 1, []

while x:
    x, p = drop_sand(grid, np.array((500,0)))
    if p == -1 and len(sols) == 0:
        sols.append(count)
    count+=1
    if grid[500,0] == 1:
        sols.append(count)
        break

print(*sols)

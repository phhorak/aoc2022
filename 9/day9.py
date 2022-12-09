import numpy as np
moves =  [(x.split()[0], int(x.split()[1])) for x in open('input').read().rstrip().split('\n')]
ks = [[np.array((0,0))] for i in range(10)]
dirs = {'R': (1,0), 'L': (-1,0), 'U': (0,1), 'D': (0,-1)}

move = lambda diff:  np.sign((diff)) if np.linalg.norm(diff) >=2 else np.array((0,0))

for dir, n in moves:
    for j in range(n):
        ks[0].append(ks[0][-1] + dirs[dir])
        for i in range(1,len(ks)):
            ks[i].append(ks[i][-1] + move(ks[i-1][-1] - ks[i][-1]))

print(len(set([tuple(x) for x in ks[1]])), len(set([tuple(x) for x in ks[9]])))

#move = lambda diff : np.round( abs((diff)/2) * min(sum(abs((diff)/2)),1.5) - 0.01) * np.sign((diff)) if sum(diff)

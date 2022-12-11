parser = lambda x : list(range(int(x.split('-')[0]),int(x.split('-')[1])+1))
data = [list(map(parser,line.split(','))) for line in [lines for lines in open('input').read().strip().split('\n')]]

subset = [set(x[0]) <= set(x[1]) or set(x[1]) <= set(x[0]) for x in data]
overlap = [len(set(x[0]) & set(x[1])) > 0 for x in data]
print(sum(subset), sum(overlap))

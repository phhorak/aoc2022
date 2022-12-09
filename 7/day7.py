from collections import defaultdict

term =  open('input').read().rstrip().split('\n')
sizes, pwd = defaultdict(int), ['/']

for line in term[1:]:
    x = line.split()
    if x[0]=='$' and x[1] == 'cd':
        if x[2] != '..':
            pwd.append(x[2]+'/')
        else:
            pwd.pop()
    elif x[0].isdigit():
        for i in range(len(pwd)):
            sizes[''.join(pwd[:i+1])] += int(x[0])

small = [i for i in sizes.values() if i <= 100000]
sort = [i for i in sorted(sizes.values()) if sizes['/'] - i <=  40000000]
print(sum(small), sort[0])

term =  open('input').read().rstrip().split('\n')
pwd, files, sizes = [], {}, {}

for line in term:
    if line[:4]=='$ cd':
        dir = line[5:]
        if dir != '..':
            if dir != '/':
                dir += '/'
            pwd.append(dir)
            if ''.join(pwd) not in files.keys():
                files[''.join(pwd)] = {}
        else:
            pwd.pop()
    elif line[:4] != '$ ls':
        size, name = line.split(' ')
        if size.isdigit():
            files[''.join(pwd)][name] = int(size)

for k in files.keys():
    sizes[k] = 0
    for j in files[k].keys():
        sizes[k] += files[k][j]

for k in files.keys():
    for j in files.keys():
        if j.startswith(k) and k!= j:
            sizes[k] += sizes[j]

smalls = [i for i in sizes.values() if i <= 100000]
sort = [i for i in sorted(sizes.values()) if i >= sizes['/'] - 40000000]
print(sum(smalls), sort[0])

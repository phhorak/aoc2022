data = [list(map(lambda x : ord(x) - 96 if x.islower() else ord(x) -38, line)) for line in [lines for lines in open('input').read().strip().split('\n')]]
groups = [data[i:i+3] for i in range(0, len(data), 3)]

sums = [list(set(line[:len(line)//2]) & set(line[len(line)//2:]))[0] for line in data]
sums2 = [list(set(line[0]) & set(line[1]) & set(line[2]))[0] for line in groups]

print(sum(sums), sum(sums2))

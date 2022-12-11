data = [map(int,elf.split('\n')) for elf in [lines for lines in open('input').read().strip().split('\n\n')]]
sums = [sum(elf) for elf in data]
print('part 1: ', max(sums), 'part 2: ', sum(sorted(sums)[::-1][:3]))

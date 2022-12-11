stacks, moves =  [lines.split('\n') for lines in open('input').read().rstrip().split('\n\n')]
move_ints = [[int(w) for w in m.split() if w.isdigit()] for m in moves]

size = int(stacks[-1][-1])*4
stacks = [[i.ljust(size)[j] for i in stacks if i.ljust(size)[j] != ' '] for j in range(1,size,4)]
stacks2 = [s[:] for s in stacks]

for move in move_ints:
    for _ in range(move[0]):
        stacks[move[2]-1] = [stacks[move[1]-1].pop(0)] + stacks[move[2]-1]
    stacks2[move[2]-1] = [stacks2[move[1]-1].pop(0) for _ in range(move[0])] + stacks2[move[2]-1]

print(''.join([s[0] for s in stacks]), ''.join([s[0] for s in stacks2]))

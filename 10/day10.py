input = open('input').read().rstrip().split('\n') + ['pad'] * 240
X, cycles, drawing = [1], [], []
for i in range(240):
    match input[i].split(' '):
        case 'addx', v: cycles += [0,int(v)]
        case ['noop']:  cycles += [0]

    drawing += '#' if abs(X[-1] - i % 40) <=1 else ' '
    X += [X[-1] + cycles.pop(0)]

print(sum([X[i-1] * i for i in range(20,240,40)]))

for d in [drawing[i:i + 40] for i in range(0, len(drawing), 40)]:
    print(''.join(d))

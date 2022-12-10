input = open('input').read().rstrip().split('\n')
X, cycles, p2 = [1], [], []
for i, l in enumerate(input + ['pad'] * (240 - len(input))):
    match l.split(' '):
        case 'addx', v: cycles += [0,int(v)]
        case ['noop']:  cycles += [0]

    p2 += '#' if abs(X[-1] - i % 40) <=1 else ' '
    X  += [X[-1] + cycles.pop(0)]

print(sum([X[i-1] * i for i in range(20,240,40)]))

for d in [p2[i:i + 40] for i in range(0, len(p2), 40)]:
    print(''.join(d))

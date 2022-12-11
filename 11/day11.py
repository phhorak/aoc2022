import numpy as np, copy
input, ms = open('input').read().replace('\n\n', '\n').rstrip().split('\n'), {}
for l in input:
    match l.split():
        case 'Monkey', number:                 ms[(key := int(number[:-1]))]  = {'inspected': 0}
        case ['Starting', 'items:', *rest]:    ms[key]['items'] = [int(r.replace(',', '')) for r in rest]
        case ['Operation:','new', '=', *rest]: ms[key]['op'] =  ' '.join(rest)
        case ['Test:', *rest]:                 ms[key]['div'] = int(rest[-1])
        case ['If', 'true:', *rest]:           ms[key]['true'] = int(rest[-1])
        case ['If', 'false:', *rest]:          ms[key]['false'] = int(rest[-1])

parts = [[20,3], [10000, np.prod([ms[m]['div'] for m in ms.keys()])]]
for p in parts:
    m = copy.deepcopy(ms)
    for r in range(p[0]):
        for k in m.keys():
            for item in m[k]['items'].copy():
                item = (lambda old: eval(m[k]['op']))(m[k]['items'].pop(0))
                item = item // p[1] if p[1] == 3 else item % p[1]
                m[k]['inspected'] +=1
                target = m[k]['false']if item %m[k]['div'] else m[k]['true']
                m[target]['items'] += [item]
    print(np.prod(sorted([m[x]['inspected'] for x in m.keys()])[::-1][:2]))

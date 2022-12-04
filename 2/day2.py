data = [list(map(lambda x : (ord(x) - 65) % 23, line.split(' '))) for line in [lines for lines in open('input').read().strip().split('\n')]]
rotate = lambda arr, n : arr[-n:] + arr[:-n]

scores = [rotate([3,6,0],line[0])[line[1]] + line[1]+1 for line in data]
scores2 = [3*line[1] + rotate([3,1,2],-line[0])[line[1]] for line in data]

print(sum(scores), sum(scores2))

scores = {'A': {'X':3+1, 'Y':6+2, 'Z': 0+3}, 'B': {'X':0+1, 'Y':3+2, 'Z': 6+3}, 'C': {'X':6+1, 'Y':0+2, 'Z': 3+3}}
scores2 = {'A': {'X':0+3, 'Y':3+1, 'Z': 6+2}, 'B': {'X':0+1, 'Y':3+2, 'Z': 6+3}, 'C': {'X':0+2, 'Y':3+3, 'Z': 6+1}}

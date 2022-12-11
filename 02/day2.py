data = [list(map(lambda x : (ord(x) - 65) % 23, line.split(' '))) for line in [lines for lines in open('input').read().strip().split('\n')]]
rotate = lambda arr, n : arr[-n:] + arr[:-n]

scores = [rotate([3,6,0],line[0])[line[1]] + line[1]+1 for line in data]
scores2 = [3*line[1] + rotate([3,1,2],-line[0])[line[1]] for line in data]

print(sum(scores), sum(scores2))

code =  open('input').read().rstrip()
msg = [[i for i in range(u,len(code)) if len(set(code[i-u:i])) == u][0] for u in [4,14]]
print(msg)

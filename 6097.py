h, w = map(int, input().split())
n = int(input())

g = []
for i in range(h):
  g.append([])
  for j in range(w):
    g[i].append(0)

for i in range(n):
  l, d, x, y = map(int, input().split())
  for j in range(l):
    if d==0:
      g[x-1][y-1+j]=1
    else:
      g[x-1+j][y-1]=1

for i in range(h):
  for j in range(w):
    print(g[i][j], end=' ')
  print()

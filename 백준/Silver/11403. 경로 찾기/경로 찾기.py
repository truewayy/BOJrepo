n = int(input())
li = []
for i in range(n):
  li.append(list(map(int, input().split())))
  
for k in range(n):
  for i in range(n):
    for j in range(n):
      if li[i][j] == 1 or (li[i][k] == 1 and li[k][j]==1):
        li[i][j] = 1

for i in li:
  for j in i:
    print(j, end=" ")
  print()
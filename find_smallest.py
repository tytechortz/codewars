def smallest(n):
  s = str(n)
  print(s)
  min1, from1, to1 = n, 0, 0
  for i in range(len(s)):
    removed = s[:i] + s[i+1:]
    print(removed)
    for j in range(len(removed)+1):
      num = int(removed[:j] + s[i] + removed[j:])
      if (num < min1):
        min1, from1, to1 = num, i, j
  print([min1, from1, to1])
  return [min1, from1, to1]


smallest(285365)
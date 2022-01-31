import itertools

for p in itertools.permutations('01234', 3):
  print(''.join(str(x) for x in p))

import itertools

for p in itertools.permutations('01234', 5):
  print(''.join(str(x) for x in p))

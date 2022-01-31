import itertools

for p in itertools.combinations('01234', 3):
  print(''.join(str(x) for x in p))

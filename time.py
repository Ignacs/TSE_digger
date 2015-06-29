# -*- coding: big5 -*-
import time, itertools

# Record start time
tStart = time.time()

# run a permutation
for item in (itertools.permutations("0123456789", 6)):
	print(''.join(item))

# Record stop time
tStop = time.time()

print(tStop - tStart)

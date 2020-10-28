# to test repl embedding
# press [play] to run

import root_finding as rf


def f(x):
  return 10 - x*x

print(rf.bisection(f, 0, 5, 1e-5))

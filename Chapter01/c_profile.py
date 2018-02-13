# from simul import benchmark
# import cProfile
#
# cProfile.run("benchmark()")
#

from simul import benchmark
import cProfilepr = cProfile.Profile()

pr.enable()
benchmark()
pr.disable()
pr.print_stats()

